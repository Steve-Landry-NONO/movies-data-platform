#!/usr/bin/env bash
# Cree l'index movies_clean avec mapping explicite et analyzer custom
# A executer apres que Elasticsearch soit up
# TODO F4 : Linda completera elasticsearch/mappings/movies_clean.json
set -e

MAPPING_FILE="elasticsearch/mappings/movies_clean.json"

if [ ! -s "$MAPPING_FILE" ]; then
  echo "[INFO] $MAPPING_FILE est vide. La feature F4 n'est pas encore livree."
  exit 0
fi

echo "Creation de l'index movies_clean..."
curl -X PUT "http://localhost:9200/movies_clean" \
  -H "Content-Type: application/json" \
  -d @"$MAPPING_FILE"
echo ""
echo "[OK] Index cree."
