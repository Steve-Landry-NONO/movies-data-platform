# Dictionnaire de donnees - movies_clean

> Owner : Linda (F4)

## Source
Les données de `movies_clean` proviennent du nettoyage appliqué au dataset `movies.csv` via le pipeline Logstash `20-clean.conf`.

## Champs disponibles dans `movies_clean`

| Champ | Type Elasticsearch | Rôle | Exemple |
|---|---|---|---|
| `movie_id` | integer | Identifiant unique du film | 278 |
| `title` | text + keyword | Titre du film pour la recherche plein texte et le filtrage exact | The Shawshank Redemption |
| `overview` | text | Résumé du film pour la recherche textuelle | Two imprisoned men bond over a number of years... |
| `original_language` | keyword | Langue originale du film | en |
| `release_date_ts` | date | Date de sortie normalisée | 1994-09-23 |
| `popularity` | float | Score de popularité | 67.4 |
| `vote_average` | float | Moyenne des votes | 8.7 |
| `vote_count` | integer | Nombre de votes | 24567 |

## Choix de modélisation

- Les champs textuels principaux (`title`, `overview`) sont définis en `text` pour permettre la recherche plein texte.
- Le champ `title` possède aussi un sous-champ `keyword` pour les filtres exacts et certains tris.
- `original_language` est défini en `keyword` car il s'agit d'une valeur catégorielle courte.
- `release_date_ts` est défini en `date` pour permettre les filtres par période.
- `popularity`, `vote_average` et `vote_count` sont typés numériquement pour rendre possibles les calculs, tris et agrégations.

## Analyzer custom

L’analyzer `movie_analyzer` est utilisé sur les champs textuels principaux.

Il applique :
- `lowercase` : mise en minuscules
- `english_stop` : suppression des stopwords anglais
- `asciifolding` : normalisation des accents

Cet analyzer améliore la qualité de la recherche textuelle sur les titres et les résumés.
