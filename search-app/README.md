# Search App

Mini moteur de recherche connecté à Elasticsearch.

## Objectif
Cette application permet d’interroger l’index `movies_clean` à travers :
- une interface web simple,
- une route API HTTP exploitable pour les tests.

Elle répond à la partie F8 du projet demandant un moteur de recherche minimal mais fonctionnel basé sur Elasticsearch.

## Fonctionnalités
- recherche full-text sur :
  - `title`
  - `overview`
- filtre exact sur :
  - `original_language`
- filtre simple par année via :
  - `release_date_ts`
- affichage des résultats avec :
  - titre
  - langue
  - date
  - popularité
  - note
  - nombre de votes
  - résumé

## Structure
Les fichiers principaux de cette feature sont :

- `search-app/app.py`
- `search-app/templates/index.html`
- `search-app/requirements.txt`
- `search-app/README.md`

## Prérequis
Avant de lancer l’application, vérifier que :

- Docker est démarré
- Elasticsearch est accessible sur `http://localhost:9200`
- l’index `movies_clean` existe et contient des documents

Exemple de vérification :

```bash
curl http://localhost:9200/movies_clean/_count
