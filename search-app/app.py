from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
import requests
from typing import Optional

app = FastAPI(title="Movies Search App")

ES_BASE_URL = "http://localhost:9200"
ES_INDEX = "movies_clean"

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


def normalize_year(year_value: Optional[str]) -> Optional[int]:
    if year_value is None:
        return None
    year_value = str(year_value).strip()
    if year_value == "":
        return None
    try:
        return int(year_value)
    except ValueError:
        return None


def build_es_query(
    q: str = "",
    language: Optional[str] = None,
    year: Optional[int] = None,
    size: int = 10
):
    must_clauses = []
    filter_clauses = []

    if q:
        must_clauses.append({
            "multi_match": {
                "query": q,
                "fields": ["title^2", "overview"],
                "type": "best_fields"
            }
        })
    else:
        must_clauses.append({"match_all": {}})

    if language:
        filter_clauses.append({
            "term": {
                "original_language": language
            }
        })

    if year:
        filter_clauses.append({
            "range": {
                "release_date_ts": {
                    "gte": f"{year}-01-01",
                    "lte": f"{year}-12-31"
                }
            }
        })

    return {
        "size": size,
        "_source": [
            "movie_id",
            "title",
            "overview",
            "original_language",
            "release_date_ts",
            "popularity",
            "vote_average",
            "vote_count"
        ],
        "query": {
            "bool": {
                "must": must_clauses,
                "filter": filter_clauses
            }
        },
        "sort": [
            {"_score": "desc"},
            {"popularity": "desc"}
        ]
    }


def search_movies(
    q: str = "",
    language: Optional[str] = None,
    year: Optional[int] = None,
    size: int = 10
):
    url = f"{ES_BASE_URL}/{ES_INDEX}/_search"
    payload = build_es_query(q=q, language=language, year=year, size=size)

    response = requests.get(url, json=payload, timeout=10)
    response.raise_for_status()
    data = response.json()

    results = []
    for hit in data.get("hits", {}).get("hits", []):
        src = hit.get("_source", {})
        results.append({
            "score": hit.get("_score"),
            "movie_id": src.get("movie_id"),
            "title": src.get("title"),
            "overview": src.get("overview"),
            "original_language": src.get("original_language"),
            "release_date_ts": src.get("release_date_ts"),
            "popularity": src.get("popularity"),
            "vote_average": src.get("vote_average"),
            "vote_count": src.get("vote_count"),
        })

    return results


@app.get("/", response_class=HTMLResponse)
def home(
    request: Request,
    q: str = Query(default=""),
    language: str = Query(default=""),
    year: str = Query(default="")
):
    error = None
    results = []

    normalized_language = language.strip() or None
    normalized_year = normalize_year(year)

    try:
        results = search_movies(
            q=q,
            language=normalized_language,
            year=normalized_year,
            size=10
        )
    except Exception as e:
        error = str(e)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "q": q,
            "language": language,
            "year": year,
            "results": results,
            "error": error
        }
    )


@app.get("/api/search", response_class=JSONResponse)
def api_search(
    q: str = Query(default=""),
    language: str = Query(default=""),
    year: str = Query(default=""),
    size: int = Query(default=10, ge=1, le=50)
):
    normalized_language = language.strip() or None
    normalized_year = normalize_year(year)

    try:
        results = search_movies(
            q=q,
            language=normalized_language,
            year=normalized_year,
            size=size
        )
        return {"ok": True, "count": len(results), "results": results}
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"ok": False, "error": str(e)}
        )