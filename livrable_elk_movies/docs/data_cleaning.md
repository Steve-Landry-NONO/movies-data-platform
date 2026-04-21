# 🧹 Rapport de Nettoyage & Impact (Data Engineering)

Ce document décrit les transformations appliquées par Logstash pour passer des données brutes CSV à l'index analytique performant `movies_clean`.

## 📊 Mesures d'Impact (Audit Qualité)

Nous avons audité le volume de données chargées :

| Métrique | Valeur | Observation |
| :--- | :--- | :--- |
| **Lignes CSV source** | 20 054 | Dataset TMDB complet. |
| **Documents `movies_raw`** | 40 108 | Ingestion brute sécurisée (doublée par le filtre Clone). |
| **Documents `movies_clean`** | 20 054 | Corresponds exactement au volume source. |
| **Taux de perte** | 0.0% | Aucune ligne n'a été rejetée par le filtre CSV. |

## 🛠️ Règles de Transformation (Pipeline ETL)

Les règles suivantes sont appliquées dans `logstash_project.conf` :

1.  **Exclusion d'En-tête** : Suppression de la ligne de titre du CSV via une regex (`/^"index","title"/`).
2.  **Typage Fort (Mutate)** :
    - `movie_id` -> `integer` (permet des jointures efficaces).
    - `popularity` & `vote_average` -> `float` (permet les aggrégations mathématiques).
    - `vote_count` -> `integer`.
3.  **Normalisation Temporelle (Date)** :
    - Conversion des formats `dd-MM-yyyy` et `yyyy-MM-dd` en un champ `release_date_ts` reconnu par Elasticsearch.
    - Cela permet l'utilisation du sélecteur de temps (Time Picker) dans Kibana.
4.  **Optimisation de l'Espace** :
    - Suppression des champs techniques Logstash (`@version`, `host`, `path`) pour ne garder que la donnée métier.

## 🧠 Mapping Explicite vs Dynamique
Contrairement au mode "Auto-mapping" d'Elasticsearch, nous avons appliqué un **Mapping Explicite** via `mapping_movies_clean.json` AVANT l'ingestion pour :
- Définir l'analyzer `movie_title_analyzer`.
- Forcer le champ `original_language` en type `keyword` (plus rapide pour les filtres du moteur de recherche).
