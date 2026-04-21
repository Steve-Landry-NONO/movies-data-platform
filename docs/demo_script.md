# Script de demo

> Owner : Radia (F9 GIF + coordination demo)

## Objectif
Montrer en 30-60 secondes que la plateforme fonctionne de bout en bout.

## Parcours filme dans demo.gif

1. Terminal : `docker compose up -d`
2. Terminal : `./scripts/healthcheck.sh` -> ES + Kibana up
3. Terminal : `curl localhost:9200/movies_raw/_count` -> 9000+
4. Terminal : `curl localhost:9200/movies_clean/_count` -> 9000+
5. Kibana : ouvrir dashboard -> montrer les visus
6. Search app : rechercher "seigneur" -> resultats
