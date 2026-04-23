# Nettoyage des donnees

> Owner : Theophane (F3)

## Anomalies observees dans movies_raw

A detailler : valeurs manquantes, formats incoherents, types mal devines, etc.

## Regles de nettoyage appliquees

A detailler dans `logstash/pipeline/20-clean.conf`.

## Mesure d'impact avant/apres

| Metrique | movies_raw | movies_clean | Commentaire |
|---|---|---|---|
| Nombre de documents | | | |
| Dates valides (release_date) | | | |
| vote_average en float | | | |
| Genres splittes en array | | | |
