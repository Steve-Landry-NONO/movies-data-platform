# 🎬 Movies Data Platform - ELK Project

Bienvenue dans le dépôt du projet Movies Data Platform. Ce dossier contient l'intégralité des livrables exploitables pour l'évaluation.

## 🚀 Démarrage Rapide

1. **Prérequis** : Docker et Docker Compose installés sur la machine.
2. **Lancer la stack** :
   ```bash
   docker compose up -d
   ```
3. **Services disponibles** :
   - **Elasticsearch** : `http://localhost:9200`
   - **Kibana** : `http://localhost:5601`
   - **Jupyter Lab** : `http://localhost:8888` (Token: `elasticlab`)

## 📂 Structure du Projet

- `docker-compose.yml` : Orchestration de la stack (ES, Kibana, Logstash, Jupyter).
- `data/` : Contient le dataset TMDB brut (`movies_dataset.csv`).
- `logstash/pipeline/` : Configuration ETL pour le nettoyage des données.
- `elasticsearch/` : Mapping explicite et analyzers personnalisés.
- `notebooks/` : Exercices de requêtes analytiques (Query DSL).
- `web/` : Interface du mini-moteur de recherche.
- `docs/` : Documentation complète (Dictionnaire, Nettoyage, Runbook, Suivi projet).

## 🛠️ Étapes de validation préconisées

1. Attendre 30-60 secondes après le lancement pour que Logstash indexe les 10 000 films.
2. Ouvrir le **Jupyter Notebook** (`notebooks/commandes_elk.ipynb`) pour tester les 12 requêtes analytiques.
3. Ouvrir l'application **Web** (`web/search_app.html`) pour tester le moteur de recherche "Luxe".
4. Importer les visualisations Kibana depuis `docs/dashboard_export.ndjson` (si disponible).

---
**Équipe de développement** :
Lead Developer : Théophanes (`theophanes@google.com`)
Groupe de projet ELK Movies.
