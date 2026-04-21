# Movies Data Platform

Projet ELK d'analyse de donnees cinematographiques (dataset TMDB ~10 000 films).

## Equipe et rôle respectif

- **Steve KOUOKAM** - Tech Lead (infra, coordination, synthese)
- **Theophane KENGNI** - Data Engineer (pipelines Logstash, nettoyage)
- **Linda MAKAMTA** - Search Engineer (mapping, analyzer, requetes DSL)
- **Radia GHILAS** - Dataviz & Search App (Kibana, moteur de recherche)

## Demarrage rapide

Pre-requis : Docker Desktop (Windows/Mac) ou Docker Engine (Linux), Git.

```bash
git clone https://github.com/<pseudo>/movies-data-platform.git
cd movies-data-platform

# Placer le dataset dans DATA/movies.csv (voir docs/runbook.md)

docker compose up -d
./scripts/healthcheck.sh     # Linux/Mac
# Windows : voir docs/runbook.md
```

URLs :
- Elasticsearch : http://localhost:9200
- Kibana : http://localhost:5601

## Documentation

- [Runbook](docs/runbook.md) : demarrage, commandes, depannage
- [Dictionnaire de donnees](docs/data_dictionary.md)
- [Nettoyage des donnees](docs/data_cleaning.md)
- [Gestion de projet](docs/project_management.md)
- [Planning poker](docs/planning_poker.md)
- [Script de demo](docs/demo_script.md)

## Stack

- Elasticsearch 8.13 + Kibana 8.13 + Logstash 8.13
- Docker Compose

## Conventions Git

- `main` : version stable (protegee, PR + 1 review requises)
- `dev` : integration (protegee, PR + 1 review requises)
- `feature/F<n>-<slug>` : developpement

Push direct sur `main` et `dev` interdit.
