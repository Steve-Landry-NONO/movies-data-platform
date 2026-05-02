# Gestion de projet

## Equipe et roles

| Membre | Role | Features | Docs owned |
|---|---|---|---|
| Steve | Tech Lead | F0, F7 consolidation, synthese, support F4/F8 | runbook.md, project_management.md, planning_poker.md, synthese |
| Theophane | Data Engineer | F2, F3 | data_cleaning.md |
| Linda | Search Engineer | F4, F5 | data_dictionary.md, requetes DSL |
| Radia | Dataviz & Search App | F6, F8, demo.gif | demo_script.md, export dashboard |

Le travail reste collaboratif : certains membres ont apporté du renfort sur des features hors de leur périmètre initial afin d’accélérer l’intégration et de stabiliser le dépôt.

## Workflow Git (Gitflow simplifie)

- Branches protegees : `main`, `dev`
- Branches features : `feature/F<n>-<slug>`
- Toutes les PR vont vers `dev`
- PR finale `dev -> main` a la fin du projet
- 1 review minimum par PR
- Commits : `feat(F<n>):`, `fix(F<n>):`, `docs(F<n>):`, `chore:`

## Rituels

- Synchro quotidienne : coordination via messages d’equipe et revues GitHub
- Planning poker : realise et consigne dans `docs/planning_poker.md`
- Revues : relectures croisees avant merge dans `dev`

## Backlog

| ID | Feature | Owner | Status | Commentaire |
|---|---|---|---|---|
| F0 | Bootstrap skeleton | Steve | DONE | Structure initiale du repo, stack de base, docs squelette |
| F1 | Docker stack | Steve | DONE | Docker Compose operationnel, healthcheck, runbook de demarrage |
| F2 | Ingestion raw | Theophane | DONE | Lecture de `movies.csv`, indexation dans `movies_raw` |
| F3 | Nettoyage pipeline | Theophane | DONE | Nettoyage, conversions de types, preparation de `movies_clean` |
| F4 | Mapping + analyzer | Linda + Steve | DONE | Mapping explicite et analyzer custom alignes avec les champs stables |
| F5 | Requetes DSL (12+) | Linda | DONE | Branche propre creee, contenu finaliser avec les 12 requetes dont 5 bool |
| F6 | Dashboard Kibana | Radia + Linda | IN PROGRESS | Export `.ndjson` present, verification visuelle/import a finaliser |
| F7 | Documentation finale | Steve | IN PROGRESS | Consolidation projet, synthese finale, relecture globale |
| F8 | Search app | Radia + Steve | TODO | Mini moteur de recherche a finaliser et demontrer |

## Implication individuelle

Chaque membre a contribue selon le decoupage suivant :
- **Steve** : setup initial, pilotage technique, integration, correction de branches, documentation projet
- **Theophane** : ingestion brute, nettoyage, documentation de nettoyage
- **Linda** : mapping, analyzer, requetes Elasticsearch
- **Radia** : dashboard Kibana, moteur de recherche, demonstration visuelle

## Etat actuel du projet

Le projet dispose deja :
- d’une stack ELK relancable localement
- d’un index `movies_raw`
- d’un index `movies_clean`
- d’un pipeline de nettoyage documente
- d’un mapping explicite avec analyzer custom
- d’une base de dashboard Kibana exportee

Les priorites restantes sont :
1. finaliser F5 (12 requetes dont 5 bool)
2. valider visuellement F6 dans Kibana
3. finaliser F8 (mini moteur de recherche)
4. produire la synthese finale et la demonstration
