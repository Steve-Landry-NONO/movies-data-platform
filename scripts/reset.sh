#!/usr/bin/env bash
# Reset complet : arrete la stack et efface toutes les donnees
set -e
echo "Arret de la stack et suppression des volumes..."
docker compose down -v
echo "Termine. Relancer avec : docker compose up -d"
