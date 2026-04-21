# Gestion de projet

## Equipe et roles

| Membre | Role | Features | Docs owned |
|---|---|---|---|
| Steve | Tech Lead | F0, F7 consolidation, synthese | runbook.md, synthese |
| Theophane | Data Engineer | F2, F3 | data_cleaning.md |
| Linda | Search Engineer | F4, F5 | data_dictionary.md |
| Radia | Dataviz & App | F6, F8, demo.gif | demo_script.md |

Le tout reste collaboratif donc il se peut que sur certaines taĉhes il ya du renforcement
Notamement Linda qui aidera en dataviz et steve sur l'apps par exemple, on verra.

## Workflow Git (Gitflow simplifie)

- Branches protegees : `main`, `dev`
- Branches features : `feature/F<n>-<slug>`
- Toutes les PR vont vers `dev`
- PR finale `dev -> main` a la fin du projet
- 1 review minimum par PR
- Commits : `feat(F<n>):`, `fix(F<n>):`, `docs(F<n>):`, `chore:`

## Rituels

- Synchro quotidienne : [a definir] (30 min)
- Planning poker : [date] (voir planning_poker.md)

## Backlog

| ID | Feature | Owner | Status |
|---|---|---|---|
| F0 | Bootstrap skeleton | Tech Lead | DONE |
| F1 | Docker stack | Tech Lead | DONE |
| F2 | Ingestion raw | Theophane | TODO |
| F3 | Nettoyage pipeline | Theophane | TODO |
| F4 | Mapping + analyzer | Linda & steve | TODO |
| F5 | Requetes DSL (12+) | Linda | TODO |
| F6 | Dashboard Kibana | Radia & Linda| TODO |
| F7 | Documentation finale | Tech Lead & Theophane | IN PROGRESS |
| F8 | Search app | Radia steve | TODO |

## Implication individuelle

Chaque membre : >= 1 PR ouverte, >= 1 PR reviewee, >= 1 feature possedee.
