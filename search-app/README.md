# Search App

Mini moteur de recherche connecté à Elasticsearch.

## Fonctionnalités
- recherche full-text sur `title` et `overview`
- filtre exact sur `original_language`
- filtre simple par année via `release_date_ts`

## Lancement

Depuis la racine du projet :

```bash
python3 -m venv search-app/.venv
source search-app/.venv/bin/activate
pip install -r search-app/requirements.txt
uvicorn search-app.app:app --reload
