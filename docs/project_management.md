# Gestion de projet

## Equipe et roles

| Membre | Role | Features | Docs owned |
|---|---|---|---|
| <Toi> | Tech Lead | F0, F7 consolidation, synthese | runbook.md, synthese |
| Theophane | Data Engineer | F2, F3 | data_cleaning.md |
| Linda | Search Engineer | F4, F5 | data_dictionary.md |
| Radia | Dataviz & App | F6, F8, demo.gif | demo_script.md |

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
| F4 | Mapping + analyzer | Linda | TODO |
| F5 | Requetes DSL (12+) | Linda | TODO |
| F6 | Dashboard Kibana | Radia | TODO |
| F7 | Documentation finale | Tech Lead | IN PROGRESS |
| F8 | Search app | Radia | TODO |

## Implication individuelle

Chaque membre : >= 1 PR ouverte, >= 1 PR reviewee, >= 1 feature possedee.
