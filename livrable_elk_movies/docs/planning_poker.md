# Planning Poker

## 1) Participants
- Membre 1: Dev 1
- Membre 2: Dev 2
- Membre 3: Dev 3
- Membre 4: Dev 4

## 2) Échelle utilisée
Fibonacci: 1, 2, 3, 5, 8, 13

## 3) Stories estimées

| ID | User Story | Votes initiaux | Estimation finale | Hypothèses | Owner |
|--- |--- |--- |--- |--- |--- |
| US-01 | F1 - Bootstrap stack | 3, 3, 2, 3 | 3 | Déjà un docker-compose existant | Dev 1 |
| US-02 | F2 - Ingestion brute | 5, 5, 8, 5 | 5 | Le format CSV de TMDB est connu | Dev 2 |
| US-03 | F3 - Nettoyage & normalisation | 8, 8, 13, 8 | 8 | Logstash gérera bien les tableaux | Dev 3 |
| US-04 | F4 - Mapping & qualité data | 5, 3, 5, 5 | 5 | La définition de l'analyzer est comprise | Dev 4 |
| US-05 | F5 - Requêtes analytiques | 5, 5, 3, 5 | 5 | Syntaxe DSL maîtrisée | Dev 1 |
| US-06 | F6 - Dataviz Kibana | 3, 5, 5, 5 | 5 | Connaissance de Lens | Dev 2 |
| US-07 | F7 - Documentation finale | 8, 5, 8, 8 | 8 | Modèles de doc disponibles | Dev 3 |
| US-08 | F8 - Moteur de recherche | 8, 13, 8, 8 | 8 | API ou UI simple sans backend lourd | Dev 4 |

## 4) Décisions de découpage
- Story : F3 - Nettoyage & normalisation
- Découpage : Séparé de l'ingestion brute car plus complexe.
- Risque : Mauvais parsing des dates et listes (genres, languages).
- Action : Travailler itérativement avec Logstash `stdout`.

## 5) Répartition finale des features
- Membre 1 : F1, F5
- Membre 2 : F2, F6
- Membre 3 : F3, F7
- Membre 4 : F4, F8
