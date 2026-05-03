# Synthèse finale : Movies Data Platform

## 1. Présentation du projet
Le projet **Movies Data Platform** consiste à concevoir une mini plateforme d’analyse de données cinématographiques basée sur la stack **ELK** (Elasticsearch, Logstash, Kibana), à partir d’un dataset TMDB d’environ 10 000 films. L’objectif est de couvrir une chaîne de traitement complète : ingestion des données, nettoyage, indexation, requêtage, visualisation et exploitation via une application de recherche. Le dépôt a été structuré autour de features dédiées, avec une consolidation progressive sur la branche `dev`. :contentReference[oaicite:0]{index=0}

## 2. Objectifs
Les objectifs principaux du projet étaient les suivants :
- mettre en place une stack ELK relançable localement ;
- ingérer un fichier CSV de films dans un index brut `movies_raw` ;
- nettoyer les données pour produire un index exploitable `movies_clean` ;
- définir un mapping explicite avec un analyzer adapté à la recherche textuelle ;
- proposer un ensemble de requêtes Elasticsearch documentées ;
- construire un dashboard Kibana lisible ;
- développer une mini application de recherche connectée à Elasticsearch ;
- documenter le projet pour rendre son exécution, sa démonstration et sa maintenance plus simples. 

## 3. Organisation de l’équipe
Le projet a été réparti entre quatre membres avec une logique de responsabilité par feature :
- **Steve** : lead technique, structuration du dépôt, documentation, consolidation et support d’intégration ;
- **Théophane** : ingestion brute et pipeline de nettoyage ;
- **Linda** : mapping Elasticsearch, analyzer custom et requêtes DSL ;
- **Radia** : dashboard Kibana, captures de visualisation et search app. 

Au cours du projet, certaines branches ont été reprises ou recentrées afin de maintenir un dépôt cohérent et mergeable. Cette logique de consolidation a permis de limiter les fichiers hors périmètre et de stabiliser la branche `dev`. 

## 4. Architecture technique
L’architecture repose sur trois briques principales :
- **Logstash**, pour l’ingestion et la transformation des données ;
- **Elasticsearch**, pour le stockage, l’indexation et la recherche ;
- **Kibana**, pour l’exploration visuelle.

Le projet est lancé via Docker Compose et documenté dans le runbook. Le pipeline est organisé autour de deux configurations Logstash principales :
- `10-raw.conf` pour l’ingestion dans `movies_raw`,
- `20-clean.conf` pour la transformation vers `movies_clean`. 

Cette architecture simple répond bien à l’objectif pédagogique du projet : démontrer le cycle complet de valorisation de données avec ELK.

## 5. Ingestion des données
La première étape a consisté à ingérer le fichier `movies.csv` dans un index brut `movies_raw`. Cette étape avait pour but de conserver une trace fidèle des données sources avant toute transformation. Le dataset est lu par Logstash depuis le répertoire `DATA/`, puis indexé dans Elasticsearch. Cette phase correspond à la feature F2. :contentReference[oaicite:5]{index=5}

L’ingestion brute permet ensuite :
- de valider la disponibilité des données ;
- de vérifier le volume de documents indexés ;
- de disposer d’un point de départ fiable pour les étapes de nettoyage.

## 6. Nettoyage et transformation
La deuxième étape a consisté à produire un index propre `movies_clean` à partir des données brutes. Ce nettoyage a été réalisé dans la feature F3 et documenté dans `docs/data_cleaning.md`. Le pipeline applique notamment :
- le renommage du champ `index` en `movie_id`,
- la conversion des types numériques,
- la normalisation des dates dans `release_date_ts`,
- la suppression de métadonnées Logstash inutiles,
- la gestion des valeurs manquantes sur certains champs. :contentReference[oaicite:6]{index=6}

L’objectif était de transformer un CSV brut en un jeu de données plus robuste, adapté aux requêtes, aux visualisations et à l’application finale.

## 7. Mapping et analyzer
La feature F4 a permis de stabiliser un mapping Elasticsearch explicite pour `movies_clean`, avec un analyzer custom adapté à la recherche textuelle. Le fichier de mapping `elasticsearch/mappings/movies_clean.json` est présent dans le dépôt consolidé. Il permet de typer correctement les champs structurants comme :
- `movie_id`,
- `title`,
- `overview`,
- `original_language`,
- `release_date_ts`,
- `popularity`,
- `vote_average`,
- `vote_count`. :contentReference[oaicite:7]{index=7}

L’ajout d’un analyzer dédié améliore la qualité des recherches full-text, en particulier sur les champs textuels tels que `title` et `overview`.

## 8. Requêtes Elasticsearch
La partie F5 fournit un jeu de requêtes DSL finales, intégrées dans :
- `queries/Requetes_DSL.http`
- `kibana/Requetes_DSL.http`

Ces requêtes couvrent plusieurs usages :
- comptage,
- consultation du mapping,
- affichage ciblé de champs,
- recherche par titre,
- recherche sur le résumé,
- filtres sur la langue,
- filtres temporels,
- filtres sur la note,
- tri par popularité,
- recherche multi-champs,
- requêtes bool. :contentReference[oaicite:8]{index=8}

Cette partie est essentielle car elle montre que les données ne sont pas seulement stockées, mais aussi réellement interrogeables selon différents besoins métiers.

## 9. Dashboard Kibana
La feature F6 apporte la couche de visualisation. Le dépôt consolidé contient :
- un export de dashboard dans `docs/dashboard_export.ndjson`,
- plusieurs captures d’écran des visualisations dans `kibana/Visualisations/`. :contentReference[oaicite:9]{index=9}

L’objectif de cette partie est de permettre une lecture rapide et visuelle du contenu de `movies_clean` :
- répartition des films par langue,
- popularité,
- notes,
- distributions diverses.

Le dashboard complète les requêtes DSL en offrant une lecture plus intuitive des données.

## 10. Mini moteur de recherche
La feature F8 constitue la brique applicative du projet. Elle ajoute une mini application de recherche développée avec **FastAPI**, composée :
- d’une interface web simple,
- d’une route API `/api/search`,
- d’un raccordement direct à l’index `movies_clean`. 

L’application permet :
- une recherche full-text sur `title` et `overview`,
- un filtre sur `original_language`,
- un filtre par année via `release_date_ts`,
- un affichage lisible des résultats avec titre, date, langue, popularité, note, votes et résumé. :contentReference[oaicite:11]{index=11}

Un correctif a également été intégré pour gérer proprement les champs de formulaire laissés vides, évitant ainsi les erreurs de validation côté FastAPI. :contentReference[oaicite:12]{index=12}

Cette brique montre une exploitation concrète des données indexées, au-delà de la seule consultation technique.

## 11. Gestion de projet
La documentation projet a été consolidée dans :
- `docs/project_management.md`,
- `docs/planning_poker.md`,
- `docs/demo_script.md`. 

Le planning poker a permis d’estimer les user stories principales du projet et de répartir les responsabilités. Les features ont été suivies dans un backlog avec statuts, commentaires et owners. La documentation reflète aussi les ajustements de périmètre réalisés en cours de projet, notamment le recentrage de certaines branches et la création d’une branche propre pour F5 afin d’éviter d’embarquer des fichiers provenant d’autres features. 

Cette structuration a été utile pour garder un historique lisible et améliorer la qualité de la branche `dev`.

## 12. Démonstration
Le fichier `docs/demo_script.md` décrit le scénario de démonstration final :
1. lancement de la stack ;
2. vérification de l’état d’Elasticsearch et Kibana ;
3. contrôle des index `movies_raw` et `movies_clean` ;
4. ouverture du dashboard Kibana ;
5. lancement de la search app ;
6. démonstration d’une recherche par mot-clé. :contentReference[oaicite:15]{index=15}

Ce parcours de démonstration met en valeur la chaîne complète :
- ingestion,
- nettoyage,
- indexation,
- analyse,
- recherche applicative.

## 13. Difficultés rencontrées
Le projet a rencontré plusieurs difficultés typiques d’un travail collaboratif sur dépôt Git :
- branches débordant sur le périmètre d’autres features ;
- conflits de structure entre branches ;
- intégrations partielles nécessitant un recentrage ;
- incohérences temporaires entre la documentation et l’état réel du dépôt ;
- différences d’environnement entre postes Linux et Windows, notamment pour le lancement local de la search app.

Ces difficultés ont été traitées progressivement par :
- une revue plus stricte du périmètre des branches,
- des branches de nettoyage ciblées,
- une consolidation documentaire continue,
- des tests réels sur plusieurs environnements.

## 14. Résultats obtenus
À la fin de cette phase de consolidation, la branche `dev` contient :
- une stack ELK relançable localement,
- un pipeline d’ingestion brut,
- un pipeline de nettoyage,
- un mapping explicite avec analyzer custom,
- un jeu de requêtes Elasticsearch,
- un export de dashboard Kibana et des captures associées,
- une mini application de recherche connectée à Elasticsearch,
- une documentation projet structurée. 

Le projet répond donc aux objectifs principaux fixés au départ.

## 15. Limites
Certaines limites restent à signaler :
- la qualité du rendu dépend encore de l’environnement local de démonstration ;
- la couche applicative reste volontairement minimale ;
- les visualisations Kibana peuvent encore être améliorées graphiquement ;
- la documentation a nécessité une forte consolidation finale pour refléter fidèlement l’état réel du dépôt.

Ces limites sont normales dans le cadre d’un projet pédagogique orienté démonstration technique.

## 16. Pistes d’amélioration
Plusieurs prolongements sont envisageables :
- enrichir le moteur de recherche avec davantage de filtres et de tri ;
- améliorer l’interface utilisateur de la search app ;
- ajouter des tests automatisés ;
- enrichir le mapping avec d’autres champs du dataset ;
- proposer des dashboards Kibana plus avancés ;
- intégrer une meilleure gestion de la qualité de données en amont.

## 17. Conclusion
Le projet **Movies Data Platform** a permis de construire une plateforme ELK simple mais complète, couvrant l’ensemble du cycle de valorisation des données :
- ingestion,
- transformation,
- indexation,
- requêtage,
- visualisation,
- exposition applicative.

Au-delà de l’aspect technique, le projet a également été un exercice de coordination, de gestion de branches, de consolidation et de documentation. Le résultat final est une base démontrable, structurée et cohérente, prête à être présentée dans le cadre de la soutenance.
