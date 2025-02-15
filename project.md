# Strava Enhanced : a new way of using Strava

Je veux changer ma manière de travailler avec Strava. Mon repo précédent fonctionne mais il n'est pas robuste. Si il foire, impossible de rejouer l'historique, de refaire proprement les choses. Le code n'est pas testé.

L'ambition est de construire un projet solide et robsute, presque au niveau portfolio, tout en appliquant les bonnes pratiques de l'exercice : tests unitaires, documentation, méthodes modernes de gestion de packages et de dépendance. Le but est également de tirer profit de mon IDE, PyCharm, qui n'est pas donné.

## Pêle-mêle

- Une sorte d'ETL clean : je load les données issues de l'API, architecture en médaillon.
  - BRONZE : données brutes issues de l'API.
  - SILVER : données transformées et propres.
  - GOLD : données utilisées dans les tableaux de bord.
- Des tests unitaires dans tous les sens, pour monter le projet le plus robuste possible.
- Un enchaînement de classes avec de belles méthodes à l'intérieur, à la manière d'Etam.
- Projets :
  - Changement des titres des activités Strava
    - Délais pour les objectifs
    - Emojis des objectifs
    - Flammes pour les jours consécutifs
    - Un émoji pour dire "reprise après x jours" ?
  - Changement des descriptions
    - LLM pour une édition de la description de mes runs.
    - Sorte de barre de complétion par rapport à un objectif déterminé : 1000km dans l'année par exemple.
    - Apparition de commentaire pour certains KPIs : barre des 200km franchies dans l'année, 2000 d+, 50h en activité, etc
- Une CI/CD aux petits oignons, avec tests unitaires et linting de code.
  - pre-commit ? Permet de tester un commit avant de le push sur le repo
- Faire un REX au taff avec ce projet, pour servir de guide aux ptits nouveaux + obtenir des améliorations.
- 