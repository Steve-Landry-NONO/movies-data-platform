# Movies Data Platform

Projet ELK d’analyse de données cinématographiques à partir d’un dataset TMDB d’environ 10 000 films.

## Objectif
L’objectif du projet est de construire une mini plateforme de valorisation de données basée sur la stack ELK, couvrant :

- l’ingestion de données CSV
- le nettoyage et la transformation
- l’indexation dans Elasticsearch
- l’écriture de requêtes DSL
- la visualisation dans Kibana
- l’exploitation via une mini application de recherche

## Equipe et roles
- **Steve KOUOKAM** — Tech Lead (infra, coordination, synthese, consolidation)
- **Theophane KENGNI** — Data Engineer (pipelines Logstash, nettoyage)
- **Linda MAKAMTA** — Search Engineer (mapping, analyzer, requetes DSL)
- **Radia GHILAS** — Dataviz & Search App (Kibana, moteur de recherche)

## Contenu du projet
Le dépôt contient notamment :

- une stack ELK dockerisée
- un pipeline d’ingestion dans `movies_raw`
- un pipeline de nettoyage vers `movies_clean`
- un mapping Elasticsearch explicite avec analyzer custom
- un jeu de requêtes DSL documentées
- un export de dashboard Kibana
- des captures d’écran des visualisations
- une mini application de recherche FastAPI connectée à Elasticsearch
- une documentation projet structurée

## Demarrage rapide
### Pre-requis
- Docker Desktop (Windows / Mac) ou Docker Engine (Linux)
- Git
- le fichier dataset placé dans `DATA/movies.csv`

### Cloner le projet
```bash
git clone https://github.com/<pseudo>/movies-data-platform.git
cd movies-data-platform
Lancer la stack
docker compose up -d
Vérifier les services

Sous Linux / Git Bash :

./scripts/healthcheck.sh

Sous Windows PowerShell :

curl.exe http://localhost:9200
curl.exe http://localhost:5601
URLs utiles
Elasticsearch : http://localhost:9200
Kibana : http://localhost:5601
Search app : http://127.0.0.1:8010 (si lancée localement)
Ce qu’il est possible de tester

Après démarrage, il est possible de :

vérifier les index movies_raw et movies_clean
exécuter les requêtes DSL fournies
ouvrir le dashboard Kibana
lancer la mini search app et rechercher un film
Verification des index
curl http://localhost:9200/movies_raw/_count
curl http://localhost:9200/movies_clean/_count
Requêtes Elasticsearch

Les requêtes DSL de démonstration sont disponibles dans :

queries/Requetes_DSL.http
kibana/Requetes_DSL.http

Elles couvrent notamment :

comptage
consultation du mapping
recherche par titre
recherche sur le résumé
filtres simples
requêtes bool
tri
Dashboard Kibana

La partie visualisation comprend :

un export de dashboard : docs/dashboard_export.ndjson
des captures d’écran dans kibana/Visualisations/

Cette partie permet de montrer une exploitation visuelle des données présentes dans movies_clean.

Search App

Une mini application de recherche a été développée avec FastAPI.

Elle permet :

une recherche full-text sur title et overview
un filtre sur original_language
un filtre par année
l’affichage des résultats avec les informations principales du film

Fichiers principaux :

search-app/app.py
search-app/templates/index.html
search-app/requirements.txt
search-app/README.md
Lancer la search app sous Linux / Git Bash
python3 -m venv search-app/.venv
source search-app/.venv/bin/activate
pip install -r search-app/requirements.txt
python -m uvicorn search-app.app:app --reload --port 8010
Lancer la search app sous Windows PowerShell
python -m venv search-app\.venv
.\search-app\.venv\Scripts\Activate.ps1
pip install -r search-app\requirements.txt
python -m uvicorn search-app.app:app --reload --port 8010

Si PowerShell bloque l’activation :

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\search-app\.venv\Scripts\Activate.ps1
Documentation
docs/runbook.md : démarrage, commandes, dépannage
docs/data_cleaning.md : nettoyage des données
docs/data_dictionary.md : dictionnaire de données et mapping
docs/project_management.md : gestion de projet
docs/planning_poker.md : estimation des user stories
docs/demo_script.md : parcours de démonstration
docs/synthese_finale.md : synthèse finale du projet
Fichiers importants
docker-compose.yml
logstash/pipeline/10-raw.conf
logstash/pipeline/20-clean.conf
elasticsearch/mappings/movies_clean.json
queries/Requetes_DSL.http
kibana/Requetes_DSL.http
docs/dashboard_export.ndjson
search-app/app.py
Stack technique
Elasticsearch 8.13
Kibana 8.13
Logstash 8.13
Docker Compose
FastAPI
Workflow Git
main : branche de livraison finale
dev : branche d’intégration
feature/F<n>-<slug> : branches de développement par feature

Règles :

pas de push direct sur main
pas de push direct sur dev
intégration via pull requests relues
Demonstration

Le script de démonstration est détaillé dans :

docs/demo_script.md

Le parcours de démonstration couvre :

lancement de la stack
vérification des services
contrôle des index
exécution de requêtes DSL
ouverture du dashboard Kibana
démonstration de la search app
Conclusion

Movies Data Platform est une plateforme ELK simple mais complète, permettant de démontrer une chaîne de traitement de données allant de l’ingestion jusqu’à la recherche et la visualisation.

Le projet met en avant :

la structuration d’un dépôt collaboratif
la mise en place de pipelines Logstash
l’utilisation d’Elasticsearch pour la recherche et l’analyse
la visualisation via Kibana
l’exposition d’une couche applicative minimale avec FastAPI
