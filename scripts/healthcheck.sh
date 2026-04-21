#!/usr/bin/env bash
# Verifie l'etat de la stack ELK
set -e

echo "=== Elasticsearch ==="
if curl -s http://localhost:9200 | grep -q "cluster_name"; then
  echo "[OK] Elasticsearch up"
else
  echo "[KO] Elasticsearch DOWN"
  exit 1
fi

echo ""
echo "=== Kibana ==="
STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:5601/api/status)
if [ "$STATUS" = "200" ] || [ "$STATUS" = "302" ]; then
  echo "[OK] Kibana up (HTTP $STATUS)"
else
  echo "[WARN] Kibana status HTTP $STATUS (peut-etre en cours de demarrage)"
fi

echo ""
echo "=== Indices ==="
curl -s "http://localhost:9200/_cat/indices?v"

echo ""
echo "=== Counts ==="
echo -n "movies_raw   : "
curl -s "http://localhost:9200/movies_raw/_count" | grep -oE '"count":[0-9]+' || echo "(index absent)"
echo -n "movies_clean : "
curl -s "http://localhost:9200/movies_clean/_count" | grep -oE '"count":[0-9]+' || echo "(index absent)"
