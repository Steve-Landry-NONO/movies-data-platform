# 📔 Dictionnaire de Données - ELK Movies Platform

Ce document détaille la structure des données stockées dans Elasticsearch après traitement par Logstash.

## Index : `movies_clean` (Données Nettoyées & Typées)

| Champ | Type Elastic | Description | Exemple |
| :--- | :--- | :--- | :--- |
| `movie_id` | `integer` | Identifiant unique du film dans la base TMDB | `299534` |
| `title` | `text` | Titre du film (analysé par `movie_title_analyzer`) | `Avengers: Endgame` |
| `title.keyword` | `keyword` | Titre exact non-analysé pour les tris/aggrégations | `Avengers: Endgame` |
| `original_language` | `keyword` | Code langue original (ISO 639-1) | `en` |
| `release_date_ts` | `date` | Date de sortie formatée en TIMESTAMP Elastic | `2019-04-24` |
| `popularity` | `float` | Score de popularité calculé par TMDB | `124.5` |
| `vote_average` | `float` | Moyenne des votes (/10) | `8.3` |
| `vote_count` | `integer` | Nombre total de votes | `15420` |
| `overview` | `text` | Synopsis complet du film (analysé en Anglais) | `After the devastating events...` |

## Index : `movies_raw` (Audit/Backup)

L'index `movies_raw` conserve une copie exacte des données entrantes sans aucun nettoyage de date ou de type (tout est en `text` par défaut), permettant un audit en cas de corruption de la source.

## Note Technique sur les Analyzers
Le champ `title` utilise l'analyzer personnalisé `movie_title_analyzer` défini dans les settings :
- **Tokenizer** : `standard`
- **Filtres** : `lowercase`, `asciifolding` (pour ignorer les accents).
