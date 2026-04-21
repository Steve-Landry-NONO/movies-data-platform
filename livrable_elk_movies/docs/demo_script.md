# 🎬 Script de Démonstration (Demo Script)

Ce document décrit le déroulement idéal pour enregistrer votre `demo.gif` et valider les critères de notation.

## Préparation
- Lancer toute la stack : `docker compose -f sandbox/docker-compose.project.yml up -d`
- Ouvrir 3 onglets :
    1.  Moteur de recherche (`search_app.html`)
    2.  Kibana Dashboard (`localhost:5601`)
    3.  Jupyter Notebook (`localhost:8888`)

---

## 🕒 Séquence de Démonstration (Durée suggérée : 45s)

### 1. Le Moteur de Recherche (15s)
- **Action** : Aller sur l'onglet du moteur de recherche.
- **Démonstration** :
    - Cliquer sur un film pour ouvrir la **Vue Détaillée (Modal)**. 
    - Montrer l'effet de flou (Glassmorphism) et les statistiques.
    - Fermer la modale.
    - Faire une recherche (ex: "Spider") et montrer la réactivité des **Filtres par Chips**.

### 2. Le Dashboard Kibana (15s)
- **Action** : Basculer sur Kibana.
- **Démonstration** :
    - Montrer le dashboard avec les 6-8 visualisations.
    - Cliquer sur un filtre (ex: une langue dans le camembert) pour montrer que tout le dashboard se met à jour dynamiquement.

### 3. La Technique (15s)
- **Action** : Basculer sur Jupyter.
- **Démonstration** :
    - Faire défiler rapidement le notebook jusqu'aux requêtes complexes (Ex 11-14).
    - Montrer que les requêtes retournent du JSON valide.

---

## 💡 Conseil pour le GIF
Utilisez un outil comme **ScreenToGif**. Réglez l'enregistrement à **10 FPS** et en **couleurs optimisées** pour que le fichier final reste léger tout en étant parfaitement fluide pour le professeur.
