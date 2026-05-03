# Gestion de projet

## Equipe et roles

| Membre | Role | Features | Docs owned |
|---|---|---|---|
| Steve | Tech Lead | F0, F1, F7 consolidation, synthese, support integration features | `README.md`, `docs/runbook.md`, `docs/project_management.md`, `docs/planning_poker.md`, synthese finale |
| Theophane | Data Engineer | F2, F3 | `docs/data_cleaning.md` |
| Linda | Search Engineer | F4, F5 | `docs/data_dictionary.md`, requetes DSL |
| Radia | Dataviz & Search App | F6, F8 | `docs/demo_script.md`, export dashboard, captures Kibana |

Le travail est reste collaboratif : certaines branches ont ete reprises, nettoyees ou finalisees avec renfort du lead technique afin de conserver un depot stable, mergeable et coherent avec le perimetre de chaque feature.

## Workflow Git (Gitflow simplifie)

- Branches protegees : `main`, `dev`
- Branches features : `feature/F<n>-<slug>`
- Toutes les pull requests intermediaires sont faites vers `dev`
- La pull request finale de livraison sera `dev -> main`
- 1 review minimum par PR
- Types de commits attendus :
  - `feat(F<n>):`
  - `fix(F<n>):`
  - `docs(F<n>):`
  - `chore:`

## Rituels

- Synchro quotidienne : coordination via messages d’equipe et revues GitHub
- Planning poker : realise et consigne dans `docs/planning_poker.md`
- Revues : relectures croisees avant merge dans `dev`
- Validation technique : verification du perimetre de chaque branche avant merge

## Backlog

| ID | Feature | Owner | Status | Commentaire |
|---|---|---|---|---|
| F0 | Bootstrap skeleton | Steve | DONE | Structure initiale du repo, stack de base, squelette documentaire |
| F1 | Docker stack | Steve | DONE | `docker-compose.yml`, healthcheck, runbook de demarrage |
| F2 | Ingestion raw | Theophane | DONE | Lecture de `movies.csv`, indexation dans `movies_raw` |
| F3 | Nettoyage pipeline | Theophane | DONE | Nettoyage des donnees, conversions de types, alimentation de `movies_clean` |
| F4 | Mapping + analyzer | Linda + Steve | DONE | Mapping explicite et analyzer custom alignes avec les champs stables |
| F5 | Requetes DSL (12+) | Linda + Steve | DONE | Requetes finales integrees proprement dans `queries/Requetes_DSL.http` et `kibana/Requetes_DSL.http` |
| F6 | Dashboard Kibana | Radia + Linda | DONE | Export dashboard present dans `docs/dashboard_export.ndjson` et captures d’ecran ajoutees |
| F7 | Documentation finale | Steve | IN PROGRESS | Consolidation des documents projet, relecture globale et alignement avec l’etat reel du depot |
| F8 | Search app | Radia + Steve | DONE | Mini moteur de recherche FastAPI + interface HTML, recherche full-text et filtres simples |

## Etat actuel du depot

La branche `dev` contient a present les livrables suivants :

- stack ELK relancable localement
- index `movies_raw`
- index `movies_clean`
- pipeline de nettoyage documente
- mapping explicite avec analyzer custom
- jeu de requetes Elasticsearch pour l’exploration de `movies_clean`
- export de dashboard Kibana
- captures d’ecran des visualisations Kibana
- mini application de recherche connectee a Elasticsearch
- documentation projet structuree

Les merges utiles deja integres dans `dev` couvrent :
- F2
- F3
- F4
- F5
- F6
- F7
- F8

La branche `main` contient une version plus ancienne du projet et devra recevoir un merge final controle depuis `dev` une fois la documentation de livraison totalement stabilisee.

## Implication individuelle

Chaque membre a contribue selon le decoupage suivant :

- **Steve**
  - structuration initiale du projet
  - pilotage technique
  - integration des branches
  - corrections de branches hors perimetre
  - consolidation documentaire
  - support sur autre features

- **Theophane**
  - ingestion brute
  - pipeline de nettoyage
  - documentation de nettoyage

- **Linda**
  - mapping Elasticsearch
  - analyzer custom
  - preparation des requetes DSL
  - Support dashbord Kibana

- **Radia**
  - dashboard Kibana
  - captures de visualisations
  - search app
  - preparation de la demonstration visuelle

## Decisions et ajustements en cours de projet

Au cours du projet, plusieurs ajustements ont ete necessaires pour conserver une branche `dev` propre :

- recentrage de certaines branches sur leur perimetre reel
- retrait de fichiers parasites issus d’autres features
- creation d’une branche propre pour integrer F5 sans remelanger F6, F7 et F8
- corrections de compatibilite entre l’interface de recherche et l’etat reel des index
- mise a jour progressive de la documentation pour suivre l’avancement reel du depot

Ces ajustements ont permis de privilegier une livraison stable et lisible plutot qu’un empilement de branches heterogenes.

## Priorites restantes avant livraison finale

Les priorites restantes sont maintenant :

1. finaliser la synthese finale du projet
2. mettre a jour et stabiliser `docs/demo_script.md`
3. effectuer une relecture globale de la documentation
4. verifier une derniere fois le depot (absence de fichiers parasites, coherence des noms, lisibilite)
5. ouvrir la pull request finale `dev -> main`

## Criteres de livraison vises

Le projet sera considere comme pret pour livraison finale lorsque :

- `dev` contient tous les livrables attendus
- la documentation est coherente avec l’etat reel du depot
- la demonstration est rejouable
- la search app fonctionne avec l’index `movies_clean`
- le dashboard Kibana est exporte et documente
- les requetes Elasticsearch sont presentes et lisibles
- la synthese finale est redigee

## Remarque finale

Le projet a evolue d’un simple squelette ELK vers une plateforme demonstrable, documentee et structuree, avec :
- ingestion
- nettoyage
- recherche
- visualisation
- documentation de pilotage

La phase restante est principalement une phase de consolidation et de livraison.
