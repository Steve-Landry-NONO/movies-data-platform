# Runbook ELK Movies Data Platform

Ce guide détaille les étapes pour démarrer et tester la pile complète localement, sans détruire le dossier `sandbox` original.

## Prérequis
- Docker et Docker Compose installés.
- Assurez-vous d'être dans le répertoire `sandbox`.

## Étape 1 : Démarrage du cluster de base
Lancez Elasticsearch et Kibana en premier lieu (sans Logstash) pour pouvoir initier le mapping proprement.
```bash
docker compose -f docker-compose.project.yml up -d elasticsearch kibana
```
Vérifiez que le cluster est en ligne :
```bash
curl -X GET "localhost:9200/_cluster/health"
```

## Étape 2 : Création du Mapping `movies_clean`
Avant d'ingérer les données, il est **impératif** de créer l'index propre de destination qui inclut notre analyzer personnalisé défini dans le fichier `mapping_movies_clean.json`.
Depuis le dossier `sandbox` :
```powershell
Invoke-RestMethod -Method Put -Uri "http://localhost:9200/movies_clean" -Body (Get-Content mapping_movies_clean.json -Raw) -ContentType "application/json"
```

## Étape 3 : Lancement de l'Ingestion (Logstash)
Maintenant que le cluster est prêt, lancez Logstash.
```bash
docker compose -f docker-compose.project.yml up -d logstash
```
Logstash va:
1. Lire les CSV depuis `/data/`.
2. Acheminer la ligne brute vers `movies_raw`.
3. Parser et convertir les champs (dates, numériques) et acheminer le résultat propre vers `movies_clean`.

## Étape 4 : Vérification
Attendez environ une minute l'ingestion de toutes les lignes, puis exécutez ces requêtes dans votre navigateur ou via `curl` :
- `http://localhost:9200/movies_raw/_count`
- `http://localhost:9200/movies_clean/_count`
Vous devriez obtenir un compte similaire sur les deux (environ 10 000).

## Étape 5 : Kibana et Tableau de Bord
Rendez-vous sur [http://localhost:5601](http://localhost:5601).

Créez un Data View ("Stack Management" > "Data Views") pour l'Index Pattern `movies_clean`.
Utilisez les requêtes du fichier `docs/queries.md` (Dev Tools) et explorez/créez vos visualisations.

1. **Importation** : Allez dans **Stack Management** > **Saved Objects**.
2. Cliquez sur **Import** et sélectionnez le fichier `docs/dashboard_export.ndjson`.
3. Cela importera automatiquement le Dashboard, les visualisations et le **Data View**.
4. Accédez au menu **Dashboard** pour visualiser les analyses pré-configurées.
