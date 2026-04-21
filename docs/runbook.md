# Runbook - Movies Data Platform

## 1. Pre-requis

- **Docker** : Docker Desktop (Windows/Mac) ou Docker Engine (Linux)
- **Git**
- **RAM** : 4 Go min libre
- **Ports libres** : 9200, 5601, 8000 (search-app)

Verifications :

```bash
docker --version
docker compose version
git --version
```

## 2. Recuperer le dataset

Source : https://www.kaggle.com/datasets/akshaypawar7/millions-of-movies/versions/67

1. Telecharger le CSV (compte Kaggle gratuit requis)
2. Renommer en `movies.csv`
3. Placer dans `DATA/movies.csv` a la racine du projet

## 3. Demarrage de la stack

### Linux / Mac

```bash
docker compose up -d
./scripts/healthcheck.sh
```

### Windows (PowerShell ou Git Bash)

```powershell
docker compose up -d
# Puis ouvrir http://localhost:9200 et http://localhost:5601 dans un navigateur
# Pour le healthcheck sous Windows, utiliser Git Bash et lancer :
# bash scripts/healthcheck.sh
```

Attendre 30 a 60 secondes au premier demarrage (Kibana met du temps).

## 4. Creer l'index `movies_clean`

```bash
./scripts/create_indices.sh     # Linux/Mac
bash scripts/create_indices.sh  # Windows via Git Bash
```

## 5. Commandes utiles

| Action | Commande |
|---|---|
| Demarrer | `docker compose up -d` |
| Arreter | `docker compose down` |
| Reset complet (efface data) | `docker compose down -v` |
| Logs Logstash | `docker compose logs -f logstash` |
| Logs Elasticsearch | `docker compose logs -f elasticsearch` |
| Voir les indices | `curl localhost:9200/_cat/indices?v` |
| Compter movies_raw | `curl localhost:9200/movies_raw/_count` |
| Compter movies_clean | `curl localhost:9200/movies_clean/_count` |

## 6. URLs

- Elasticsearch : http://localhost:9200
- Kibana : http://localhost:5601
- Search App : http://localhost:8000 (quand lancee)

## 7. Depannage

### Elasticsearch crashe au demarrage

- Verifier la RAM allouee a Docker Desktop (Settings -> Resources)
- Reduire `ES_JAVA_OPTS` dans `docker-compose.yml` de `-Xms1g -Xmx1g` a `-Xms512m -Xmx512m`

### Logstash n'ingere rien

- Verifier que `DATA/movies.csv` existe
- Verifier les logs : `docker compose logs logstash | grep -i error`
- Reset : `docker compose down -v` puis `docker compose up -d`

### Port deja utilise

Changer le port cote hote dans `docker-compose.yml` (ex: `"9201:9200"`)
puis utiliser `localhost:9201`.
