# Planning Poker

## 1) Participants
- Steve KOUOKAM
- Theophane KEGNI
- Linda MAKAMTA
- Radia GHILAS

## 2) Echelle utilisee
Fibonacci : 1, 2, 3, 5, 8, 13

## 3) Stories estimees

| ID | User Story | Votes initiaux | Estimation finale | Hypotheses | Owner |
|---|---|---|---|---|---|
| US-01 | En tant que dev, je veux une stack ELK dockerisee pour developper localement | 3, 3, 5, 3 | 3 | Docker Desktop / Docker Engine fonctionne sur chaque machine | Steve |
| US-02 | En tant que data eng, je veux ingerer movies.csv dans movies_raw | 3, 5, 5, 3 | 5 | Le dataset est disponible et correctement place dans DATA/movies.csv | Theophane |
| US-03 | En tant que data eng, je veux un pipeline de nettoyage vers movies_clean | 5, 8, 8, 5 | 8 | Les colonnes du dataset TMDB restent conformes et les anomalies sont gerables | Theophane |
| US-04 | En tant que dev search, je veux un mapping explicite avec analyzer custom | 3, 5, 5, 3 | 5 | Le mapping peut etre adapte depuis le cours et l'analyzer est testable facilement | Linda |
| US-05 | En tant qu'analyste, je veux 12 requetes DSL commentees dont 5 bool | 5, 5, 8, 5 | 5 | Les donnees de movies_clean sont bien types et exploitables | Linda |
| US-06 | En tant qu'utilisateur, je veux un dashboard Kibana avec 6-8 visus | 3, 5, 5, 5 | 5 | L'index pattern Kibana est cree sans blocage et les champs utiles sont exploitables | Radia |
| US-07 | En tant qu'utilisateur, je veux rechercher un film via une API/UI | 3, 5, 5, 3 | 5 | Une version simple FastAPI ou UI minimale suffit pour valider l'exigence | Radia |
| US-08 | En tant qu'evaluateur, je veux pouvoir relancer le projet depuis zero | 3, 3, 5, 3 | 3 | Le runbook est mis a jour au fil de l'eau et le projet reste stable | Steve |

## 4) Decisions de decoupage

- Story : US-01
  - Decoupage : bootstrap du repo, docker-compose, scripts utilitaires, documentation initiale
  - Risque : differences Linux / Windows
  - Action : .gitattributes + Git Bash + runbook clair

- Story : US-02
  - Decoupage : lecture CSV, pipeline raw, test _count, test _search
  - Risque : mauvais chemin du CSV ou parsing incomplet
  - Action : imposer DATA/movies.csv et faire des verifications rapides

- Story : US-03
  - Decoupage : conversions de types, parsing date, normalisation des listes, gestion des valeurs manquantes
  - Risque : champs complexes comme genres, keywords, credits
  - Action : faire simple, documenter avant/apres dans data_cleaning.md

- Story : US-04
  - Decoupage : mapping explicite, choix text/keyword, analyzer custom
  - Risque : erreurs de typage ou analyzer mal configure
  - Action : reprendre le cours du prof comme base et tester avec _mapping / _analyze

- Story : US-05
  - Decoupage : requetes simples, bool, aggregations
  - Risque : certaines requetes dependent fortement du nettoyage
  - Action : commencer par les plus simples puis monter en complexite

- Story : US-06
  - Decoupage : visualisations unitaires puis dashboard complet
  - Risque : dashboard peu lisible ou trop ambitieux
  - Action : limiter a 6-8 visus pertinentes

- Story : US-07
  - Decoupage : recherche full-text + 1 filtre simple
  - Risque : perdre trop de temps sur l'interface
  - Action : faire une version minimale et demonstrable

- Story : US-08
  - Decoupage : runbook, script de demo, verification sur machine vierge
  - Risque : oublis dans les prerequis ou les commandes
  - Action : faire un dry-run avant le rendu

## 5) Repartition finale des features

- Steve
  - F0 Bootstrap skeleton
  - F1 Docker stack operationnelle
  - F7 Documentation finale et synthese
  - Coordination et reviews

- Theophane
  - F2 Ingestion raw
  - F3 Nettoyage et normalisation
  - Contribution a docs/data_cleaning.md

- Linda
  - F4 Mapping explicite + analyzer custom
  - F5 Requetes DSL
  - Contribution a docs/data_dictionary.md

- Radia
  - F6 Dashboard Kibana
  - F8 Mini moteur de recherche
  - demo.gif et docs/demo_script.md

## 6) Conclusion de la session
L'equipe a choisi de prioriser :
1. la stack ELK fonctionnelle,
2. l'ingestion brute,
3. le nettoyage et le mapping,
4. les requetes analytiques,
5. le dashboard Kibana,
6. le mini moteur de recherche,
7. la documentation finale et la demonstration.

Compte tenu de la deadline proche, l'equipe privilegie une solution simple, propre, documentee et reproductible.
