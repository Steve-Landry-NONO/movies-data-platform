# Planning Poker

## 1) Participants
- Steve KOUOKAM
- Theophane KENGNI
- Linda MAKAMTA
- Radia GHILAS

## 2) Echelle utilisee
Fibonacci : 1, 2, 3, 5, 8, 13

## 3) Stories estimees

| ID | User Story | Votes initiaux | Estimation finale | Hypotheses | Owner |
|---|---|---|---|---|---|
| US-01 | En tant que dev, je veux une stack ELK dockerisee pour developper localement | 3, 5, 5, 3 | 5 | Docker deja vu en cours, mais risques de configuration locale | Steve |
| US-02 | En tant que data engineer, je veux ingerer `movies.csv` dans `movies_raw` pour conserver une trace brute des donnees | 3, 5, 5, 3 | 5 | CSV exploitable sans changement majeur de structure | Theophane |
| US-03 | En tant qu’analyste data, je veux nettoyer les donnees et les indexer dans `movies_clean` afin de produire des analyses fiables | 5, 8, 8, 5 | 8 | Nettoyage plus complexe que prevu : dates, types, valeurs manquantes | Theophane |
| US-04 | En tant que dev search, je veux definir un mapping explicite avec analyzer custom pour fiabiliser la recherche | 3, 5, 5, 3 | 5 | Les champs stables de `movies_clean` restent limites mais suffisants | Linda |
| US-05 | En tant qu’analyste, je veux 12 requetes Elasticsearch commentees dont 5 bool pour repondre a des besoins metier | 5, 8, 5, 5 | 5 | Les champs disponibles dans `movies_clean` permettent des cas d’usage simples mais pertinents | Linda |
| US-06 | En tant qu’utilisateur, je veux un dashboard Kibana avec 6 a 8 visualisations lisibles | 5, 5, 8, 5 | 5 | L’import/export Kibana ne pose pas de probleme majeur | Radia |
| US-07 | En tant qu’utilisateur, je veux un mini moteur de recherche connecte a Elasticsearch avec recherche full-text et filtre simple | 3, 5, 8, 5 | 5 | Une version minimale suffit pour satisfaire le sujet | Radia |
| US-08 | En tant qu’evaluateur, je veux pouvoir relancer le projet depuis zero grace a une documentation claire | 3, 5, 5, 3 | 5 | Le runbook reste simple si la stack ne change pas fortement | Steve |

## 4) Decisions de decoupage

- **Story : US-01 / US-02**
  - **Decoupage** : separer le bootstrap stack de l’ingestion brute
  - **Risque** : confusion entre problemes Docker et problemes Logstash
  - **Action** : livrer F0/F1 avant toute ingestion

- **Story : US-03**
  - **Decoupage** : nettoyer d’abord les champs essentiels seulement (`movie_id`, `title`, `overview`, `original_language`, `release_date_ts`, `popularity`, `vote_average`, `vote_count`)
  - **Risque** : vouloir traiter trop de colonnes non stabilisees
  - **Action** : recentrer la pipeline sur les champs reellement utilises

- **Story : US-04 / US-05**
  - **Decoupage** : finir le mapping avant de stabiliser les requetes
  - **Risque** : requetes faites sur des champs non presents ou mal types
  - **Action** : aligner F5 sur les champs stables issus de F3/F4

- **Story : US-06 / US-07**
  - **Decoupage** : produire une version simple mais demonstrable
  - **Risque** : surinvestissement visuel ou applicatif
  - **Action** : viser un dashboard lisible et une search app minimale

- **Story : US-08**
  - **Decoupage** : documentation alimentee tout au long du projet
  - **Risque** : doc laissee pour la fin
  - **Action** : mise a jour continue des fichiers `docs/`

## 5) Repartition finale des features
- **Steve** : F0, F1, F7 consolidation, synthese, coordination technique
- **Theophane** : F2, F3
- **Linda** : F4, F5
- **Radia** : F6, F8

## 6) Ajustements en cours de projet

Au cours du projet, certaines branches ont ete reprises ou nettoyees par le lead technique afin :
- d’aligner les branches avec le perimetre attendu de chaque feature
- de limiter les conflits et les fichiers hors sujet
- d’accelerer la stabilisation de la branche `dev`

Ces ajustements ont ete faits pour conserver une livraison propre, traçable et mergeable.
