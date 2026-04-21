# Requêtes Elasticsearch

À exécuter dans l'onglet **Dev Tools** de Kibana (`http://localhost:5601/app/dev_tools#/console`).

## 1. Requête simple (match)
Recherche d'un film incluant "spider" dans son titre.
```json
GET movies_clean/_search
{
  "query": {
    "match": {
      "title": "spider"
    }
  }
}
```

## 2. Match Phrase
Recherche de l'expression exacte "spider-man".
```json
GET movies_clean/_search
{
  "query": {
    "match_phrase": {
      "title": "spider-man"
    }
  }
}
```

## 3. Requête Bool : Must & Filter (1/5)
Trouver les films dont le titre contient "batman" sortis après 2005.
```json
GET movies_clean/_search
{
  "query": {
    "bool": {
      "must": [
        { "match": { "title": "batman" } }
      ],
      "filter": [
        { "range": { "release_date_ts": { "gte": "2005-01-01" } } }
      ]
    }
  }
}
```

## 4. Requête Bool : Should & Must_not (2/5)
Films très populaires, qui parlent d'aliens, mais pas d'anglais original.
```json
GET movies_clean/_search
{
  "query": {
    "bool": {
      "must": [
        { "match": { "overview": "alien" } }
      ],
      "should": [
        { "range": { "popularity": { "gte": 500 } } }
      ],
      "must_not": [
        { "term": { "original_language": "en" } }
      ]
    }
  }
}
```

## 5. Requête Bool : Combinaison de langues et votes (3/5)
Films japonais (ja) ou français (fr) ayant une note > 8.
```json
GET movies_clean/_search
{
  "query": {
    "bool": {
      "must": [
        { "range": { "vote_average": { "gte": 8.0 } } }
      ],
      "should": [
        { "term": { "original_language": "ja" } },
        { "term": { "original_language": "fr" } }
      ],
      "minimum_should_match": 1
    }
  }
}
```

## 6. Requête Bool : Recherche par description/synopsis (4/5)
Les films de zombie ayant des votes significatifs (>1000 votes).
```json
GET movies_clean/_search
{
  "query": {
    "bool": {
      "must": [
        { "match": { "overview": "zombie" } }
      ],
      "filter": [
        { "range": { "vote_count": { "gte": 1000 } } }
      ]
    }
  }
}
```

## 7. Requête Bool : Favoris Récents (5/5)
Films sortis depuis 2020 avec plus de 9/10, soit en anglais soit en espagnol.
```json
GET movies_clean/_search
{
  "query": {
    "bool": {
      "filter": [
        { "range": { "release_date_ts": { "gte": "2020-01-01" } } },
        { "range": { "vote_average": { "gte": 9.0 } } }
      ],
      "should": [
        { "term": { "original_language": "en" } },
        { "term": { "original_language": "es" } }
      ],
      "minimum_should_match": 1
    }
  }
}
```

## 8. Aggrégation de Termes (Langues)
Quelles sont les langues originales les plus représentées ?
```json
GET movies_clean/_search
{
  "size": 0,
  "aggs": {
    "langues_freq": {
      "terms": {
        "field": "original_language",
        "size": 5
      }
    }
  }
}
```

## 9. Aggrégation de Métriques (Global)
Moyenne globale des notes de tout le catalogue ingéré.
```json
GET movies_clean/_search
{
  "size": 0,
  "aggs": {
    "avg_rating": {
      "avg": {
        "field": "vote_average"
      }
    }
  }
}
```

## 10. Aggrégation : Histogramme sur l'âge des films
Répartition des sorties de films par décennies.
```json
GET movies_clean/_search
{
  "size": 0,
  "aggs": {
    "films_par_decennie": {
      "date_histogram": {
        "field": "release_date_ts",
        "calendar_interval": "10y"
      }
    }
  }
}
```

## 11. Multi-match query
Chercher "magic" dans le titre OU l'overview (priorité titre via un boost ^3).
```json
GET movies_clean/_search
{
  "query": {
    "multi_match": {
      "query": "magic",
      "fields": ["title^3", "overview"]
    }
  }
}
```

## 12. Fuzzy Match
Tolérance de frappe (par exemple "spiider" pour "spider").
```json
GET movies_clean/_search
{
  "query": {
    "match": {
      "title": {
        "query": "spiider",
        "fuzziness": "AUTO"
      }
    }
  }
}
```
