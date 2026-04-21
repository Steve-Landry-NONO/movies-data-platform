# Synthèse du Projet ELK - Movies Data Platform

## 1. Contexte, objectifs et périmètre
**Problème traité** : La disponibilité massive de données cinématographiques nécessite des outils robustes pour l'ingestion, le nettoyage, et l'analyse rapide en quasi temps-réel.
**Objectifs techniques/métier** : Déployer une plateforme exploitant la Stack ELK (Elasticsearch, Logstash, Kibana) afin d'ingérer environ 10 000 films du dataset TMDB, assurer la traçabilité et la qualité des données, et fournir un tableau de bord analytique aux experts métiers, couplé à un mini-moteur de recherche pour explorateur de la donnée finie.
**Périmètre** : Le projet inclut l'architecture d'ingestion Logstash bi-index (prouvant la conservation historique brute), les filtres Elasticsearch et l'interface Web finale (Vanilla HTML/JS). La mise en place de la pile respecte des standards exigeants partagés de bout en bout avec Gitflow.

## 2. Architecture et environnement
**Schéma de la stack ELK** :
L'environnement local (`sandbox`) redessiné pour la production s'articule autour de 3 conteneurs Docker configurés en code en tant qu'Infrastructure :
- **Elasticsearch (8.10.2)** : Cœur NoSQL, moteur d'analyse et d'indexation configuré en Single Node.
- **Logstash (8.10.2)** : Pipeline ETL (Extract, Transform, Load) autonome en charge de relier la donnée dormante vers Elastic.
- **Kibana (8.10.2)** : Plateforme de visualisation offrant du requêtage DSL complet.

**Flux de données** : Le fichier CSV monte statiquement (ro) dans le conteneur Logstash. Le pipeline est paramétré de manière dualiste : dès création du document structuré, la ligne `clonée` passe les étapes de filtres pour correspondre à un target index de type propre (`movies_clean`), pendant que le strict brut part tel quel sous `movies_raw`. Le dashboard Kibana et l'outil `search_app.html` pointent spécifiquement sur la racine métier nettoyée.

## 3. Données et nettoyage (Obligatoire)
**Description des données** : Le fichier CSV utilisé, une extraction TMDB, présente les colonnes vitales `movie_id`, `title`, `original_language`, `release_date`, `popularity`, `vote_average`, `vote_count` et `overview`.

**Anomalies et typages non voulus initiaux** : 
1. Logstash ingère arbitrairement la ligne d'en-tête du fichier comme s'il s'agissait du premier film.
2. Elasticsearch assigne dynamiquement la variable textuelle `String` à toutes les observations numériques brutes (moyennes de votes, ID).
3. Le format temporel `release_date` n'est pas formatable par défaut sur un histogramme.

**Règles Logstash appliquées** : 
Un conditionnel avec `drop { }` supprime l'en-tête au sein de Logstash. Le traitement s'attaque ensuite au cœur du problème via le bloc de mutation : la chaîne de caractères `vote_average` migre vers la notation `float`. L'outil `date` transforme intelligemment des configurations mixtes de dates (tel que le jour-mois-année européen) vers un objet DateTime protégé `release_date_ts`. 

**Mesure de l'Impact Avant / Après** : 
- **Avant** : `movies_raw` contient une colonne texte "05-06-2023", impossible à cibler dans une timeline "supérieur à l'an 2000". `vote_count` interdisait la recherche par intervalle.
- **Après** : `movies_clean` révèle le champ `release_date_ts` reconnu nativement par Kibana en Date object. De la même méthode, les `vote_average` s'additionnent mathématiquement pour générer des metrics (`avg`).

## 4. Modélisation Elasticsearch
L'index métier s'appuie sur le fichier JSON `mapping_movies_clean.json` (qui sera poussé lors de l'initialisation du pipeline).
**Texte versus Mot-Clef** : La métadonnée linguistique (`original_language`) a été modifiée en type `keyword`. Son utilisation stricte est de grouper ou de filtrer sans analyse lexicale.
**Analyzer personnalisé ("movie_title_analyzer")** : Ce filtre exclusif affectera le composant `title`. Il convoque le parser `standard` natif ainsi que les filtres `lowercase` et `asciifolding`. Traduction : "Léa" et "lea" ou encore "MATRIX" se transformeront tous vers une même empreinte de comparaison, garantissant aucun faux négatif d'accès à la recherche finale.

## 5. Requêtes et analyses
Le dépôt archive un fichier `docs/queries.md` totalisant 12 interrogations (les fameuses DSL), illustrant la souplesse d'Elasticsearch.
- **Construites Boolean Query (Must, Should, Filter)**. Nous avons testé des exclusions franches grâce à `must_not` pour enlever spécifiquement la langue anglaise de la recherche, mixé avec un filtrage minimum de votes pour garantir un standard de qualité.
- **Réalisations analytiques et "fuzzy"**. D'autres tests confirment la fonction `fuzziness: "AUTO"`, rattrapant des requêtes mal écrites de potentiels utilisateurs, ainsi que la capacité inestimable de générer un `date_histogram` pour cartographier le temps. L'intégration de multi-match confère une importance 3 fois supérieure sur un "Hit" ciblant le titre, plus pertinent face au synopsis entier.

## 6. Dashboard Kibana et lecture métier
Un tableau de bord, s'appuyant à chaque fois sur le catalogue nettoyé, illustre la portée :
1. **Évolution cinématographique (Date Histogram)** : Mesure des productions et des récessions temporelles (baisse ponctuelle en conjoncture historique, montée exponentielle en l'an 2000).
2. **Top Qualifications Métier (Bar chart)** : Affichage du meilleur classement (moyenne) bloqué sous exigence de minimum 1000 votes.
3. **Partitionnement linguistique (Pie Chart)** : Représentation très visuelle de l'écrasante supériorité mondiale de la langue `en` de la base TMDB.

*Limites d'interprétation* : En l'absence de colonnes d'expertise tel que les genres, acteurs spécifiques ou budget du dataset en place, la transversalité des suggestions pour l'utilisateur reste assez cantonnée aux appréciations populaires.

## 7. Gestion de projet et collaboration
Le développement de cette infrastructure a embrassé d'emblée la modalité moderne Agile et respecté le document `docs/project_management.md`. 
Nous nous sommes accordés sur **Gitflow**. La branche `dev` ne peut pas être alimentée sans un vote sur la Pull Request et la création de Features unicités (`feature/bootstrap-stack`). Nous avons chiffré ensemble une estimation complète du temps de projet en adoptant la hiérarchie de Fibonacci couchée sur `planning_poker.md`.

## 8. Bilan, limites et améliorations
**Limites** : Malgré nos bons résultats de bout-en-bout, le démarrage Docker exige encore qu'un Opérateur lance la requête Kibana pour mapper l'Index avant de déclencher l'Ingestion via Logstash (sous peine de subir le mapping dynamique par défaut).
**Amélioration 1 (Sécurité & Auth)** : Activer les contrôles de xPack. Actuellement "false", la base de données ne doit jamais être exposée de fait en clair. Les variables du docker-compose subiraient une passe drastique sur des secrets.
**Amélioration 2 (Scoring intelligent)** : La WebApp API/UI ne fait que classer par popularité textuelle sur le multi-search; Elasticsearch permet d'injecter un véritable script de scoring pour propulser en tête d'affiche les films récents avec hauts votes, contre-balançant les termes lexicaux exacts.
