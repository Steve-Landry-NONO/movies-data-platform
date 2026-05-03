# Script de demo

> Owner principal : Radia  
> Coordination demo / consolidation finale : Steve

## Objectif
Montrer en moins de 2 minutes que la plateforme fonctionne de bout en bout :

- lancement de la stack ELK
- verification de la sante des services
- presence des donnees dans `movies_raw`
- presence des donnees nettoyees dans `movies_clean`
- visualisation dans Kibana
- recherche via la search app

L’objectif n’est pas de tout montrer en detail, mais de prouver que le projet est fonctionnel, relancable et coherent.

## Pre-requis
Avant la demonstration, verifier que :

- Docker est lance
- le dataset `DATA/movies.csv` est bien present
- la branche utilisee est `dev`
- la stack peut etre relancee proprement
- la search app peut etre demarree
- Kibana est accessible

## Parcours de demonstration

### Etape 1 : montrer le depot

Depuis le terminal :

```bash id="0lm4tv"
git checkout dev
git pull

Dire rapidement :

le projet est organise en plusieurs features
la branche dev contient la version consolidee de travail
la branche main recevra la livraison finale

### Etape 2 : lancer la stack

Dans le terminal :

docker compose up -d

Puis attendre quelques secondes.

### Etape 3 : verifier la sante des services

Sous Linux / Git Bash :

./scripts/healthcheck.sh

Sous Windows PowerShell, utiliser au minimum :

curl.exe http://localhost:9200
curl.exe http://localhost:5601

Message a faire passer :

Elasticsearch est accessible
Kibana est accessible
la stack est bien demarree

### Etape 4 : verifier les index

Dans le terminal :

curl http://localhost:9200/movies_raw/_count
curl http://localhost:9200/movies_clean/_count

Message a faire passer :

movies_raw contient les donnees brutes
movies_clean contient les donnees nettoyees
le pipeline de transformation fonctionne
Etape 5 — montrer rapidement les requetes Elasticsearch

Ouvrir le fichier des requetes :

queries/Requetes_DSL.http
ou kibana/Requetes_DSL.http

Montrer rapidement :

une requete simple de comptage
une requete de recherche
une requete avec filtre
une requete bool

Message a faire passer :

le projet ne se limite pas a l’ingestion
il propose aussi un jeu de requetes DSL documentees et reutilisables
Etape 6 — ouvrir Kibana

Ouvrir :

http://localhost:5601

Montrer :

le dashboard exporte / importe
quelques visualisations lisibles
les captures d’ecran disponibles dans kibana/Visualisations si besoin

Exemples de commentaires :

repartition par langue
popularite
notes
tendances ou distribution des films

Message a faire passer :

la couche visualisation est presente
les donnees nettoyees sont exploitables dans Kibana

### Etape 7 : lancer la search app

Sous Linux / Git Bash :

python3 -m venv search-app/.venv
source search-app/.venv/bin/activate
pip install -r search-app/requirements.txt
python -m uvicorn search-app.app:app --reload --port 8010

Sous Windows PowerShell :

python -m venv search-app\.venv
.\search-app\.venv\Scripts\Activate.ps1
pip install -r search-app\requirements.txt
python -m uvicorn search-app.app:app --reload --port 8010

Si PowerShell bloque l’activation :

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\search-app\.venv\Scripts\Activate.ps1

### Etape 8 : montrer la recherche

Ouvrir :

http://127.0.0.1:8010

Effectuer une ou deux recherches simples, par exemple :

titanic
Spider

Puis montrer :

recherche full-text
filtre langue
filtre annee
resultats affiches avec titre, langue, date, popularite, note, votes et resume

Message a faire passer :

une interface simple a ete construite
elle interroge bien l’index movies_clean
elle constitue une demonstration applicative du travail realise
