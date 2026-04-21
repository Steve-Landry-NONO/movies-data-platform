# Gestion de Projet

## Stratégie Gitflow Globale

Branches utilisées :
- `main` : Ne contient que du code testé, stable et fonctionnel (production).
- `dev` : Branche d'intégration pour nos features. Sert d'environnement de staging.
- `feature/*` : Branches de travail isolées pour les user stories. Ex: `feature/bootstrap-stack`.

## Workflow de développement
1. Création systématique de branche `feature/<id>-<slug>` fonctionnelle depuis la base de `dev`.
2. Push des commits réguliers, clairs et unitaires sur la branche.
3. Ouverture d'une Pull Request (PR) vers `dev`.
4. Revue de code par au moins un autre membre de l'équipe (Review).
5. Merge de la PR et suppression de la branche distante.

## Revue de Code (Reviews)
Afin de minimiser la dette technique, le processus de revue de code consiste en :
- S'assurer que le code de la fonctionnalité implémente bien 100% des critères d'acceptation définis.
- Vérifier que la stack Elastic (ex: exécution de `docker compose up -d`) démarre correctement après les nouveaux ajouts locaux.
- Mettre à jour au besoin la documentation attenante à la feature.
