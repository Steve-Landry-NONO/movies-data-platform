# Nettoyage des donnees

> Owner : Theophane (F3)

## Anomalies observees dans movies_raw

Après l'ingestion brute dans `movies_raw` (F2), nous avons observé les anomalies suivantes dans le dataset `movies.csv` :
- **Types de données non optimaux** : Tous les champs sont ingérés comme des chaînes de caractères par défaut par Logstash, ce qui n'est pas idéal pour les analyses numériques ou les recherches par date.
- **Formats de date incohérents** : Le champ `release_date` peut avoir des formats différents (par exemple, `dd-MM-yyyy` ou `yyyy-MM-dd`), nécessitant une normalisation.
- **Valeurs manquantes** : Certains champs numériques ou de date peuvent être vides, ce qui peut entraîner des erreurs de parsing ou des types incorrects si non gérés explicitement.
- **Champs superflus** : Logstash ajoute des champs de métadonnées (`type`, `@version`, `host`, `path`, `message`, `tags`) qui ne sont pas pertinents pour l'index `movies_clean`.
- **Nom de colonne générique** : La colonne `index` du CSV est un identifiant unique qui devrait être renommé pour plus de clarté.
# - **Genres non structurés** : Si un champ `genres` existait, il serait probablement une chaîne de caractères à séparer en tableau. (Note: Le dataset `movies.csv` actuel ne contient pas de colonne `genres`. Cette règle sera appliquée si un tel champ est introduit à l'avenir.)

## Regles de nettoyage appliquees

Les règles de nettoyage suivantes sont appliquées dans `logstash/pipeline/20-clean.conf` pour transformer les données brutes en une version propre et exploitable :
- **Renommage de colonne** : La colonne `index` du CSV est renommée en `movie_id` pour une meilleure sémantique.
- **Gestion des valeurs manquantes** : Avant la conversion de type, les champs `popularity`, `vote_average`, `vote_count` et `release_date` sont vérifiés. Si une valeur est une chaîne vide, le champ est supprimé de l'événement pour éviter les erreurs de conversion et permettre à Elasticsearch de gérer l'absence de valeur.
- **Conversion de types** :
    - `movie_id` est converti en `integer`.
    - `popularity` est converti en `float`.
    - `vote_average` est converti en `float`.
    - `vote_count` est converti en `integer`.
- **Normalisation des dates** : Le champ `release_date` est parsé en un format de date standard (`yyyy-MM-dd`) et stocké dans un nouveau champ `release_date_ts` (timestamp). Le champ `release_date` original est ensuite supprimé.
- **Suppression des champs de métadonnées** : Les champs internes de Logstash (`type`, `@version`, `host`, `path`, `message`, `tags`) sont supprimés pour garder l'index `movies_clean` propre et pertinent.
# - **Traitement des genres** : (Note: Cette règle sera implémentée si un champ `genres` est ajouté au dataset. L'objectif serait de le splitter en un tableau de chaînes de caractères.)

## Mesure d'impact avant/apres

| Metrique | movies_raw | movies_clean | Commentaire |
|---|---|---|---|
| Nombre de documents | 9000+ | 9000+ | Le nombre de documents reste le même, aucune perte de données. |
| Dates valides (release_date) | String (formats variés) | Date (ISO 8601 en `release_date_ts`) | Le champ `release_date` est normalisé et converti en un type `date` exploitable. |
| vote_average en float | String | Float | Le champ `vote_average` est correctement typé pour les calculs. |
| popularity en float | String | Float | Le champ `popularity` est correctement typé pour les calculs. |
| vote_count en integer | String | Integer | Le champ `vote_count` est correctement typé pour les calculs. |
| Champs de métadonnées | Présents | Supprimés | L'index `movies_clean` est plus léger et contient uniquement les données pertinentes. |
| Gestion des valeurs manquantes | Chaînes vides ou nulles | Champs supprimés (pour les numériques/dates) | Évite les erreurs de typage et permet une meilleure gestion des données. |
| Genres splittes en array | N/A | N/A | (Note: Cette métrique est en attente de l'ajout d'un champ `genres` au dataset.) |
