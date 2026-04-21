# Dictionnaire de donnees - movies_clean

> Owner : Linda (F4)

## Source
Dataset TMDB (10 000 films), fichier CSV original : `DATA/movies.csv`.

## Schema movies_clean

| Champ | Type ES | Analyzer | Description | Exemple |
|---|---|---|---|---|
| id | integer | - | Identifiant TMDB | 278 |
| title | text + keyword | film_text_analyzer | Titre du film | "The Shawshank Redemption" |
| ... | | | | |

## Analyzer custom `film_text_analyzer`

A detailler (tokenizer, filtres, impact).
