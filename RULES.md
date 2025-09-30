# 📦 RULES DU PROJET (Version PRO)

## Objectif
Fournir une structure propre, minimaliste et reproductible pour les applications contenues dans ce dépôt.  
Tout le code applicatif est centralisé sous `build/app/`. Le dossier `build/deploy/` contient les fichiers de déploiement/développement.

## Arborescence obligatoire
- `docker-compose.yml` à la racine (production/base)
- `build/app/` :
  - `Dockerfile`
  - `app.py`
  - `requirements.txt`
  - `parsing/`
  - `templates/*.html`
  - `tests/main.py`
- `build/deploy/` :
  - `README.md` (déploiement/dev)
  - `docker-compose.dev.yml`
- `.github/workflows/docker-publish.yml` : build → test → publish
- `README.md` (racine) : doc principale

## Conventions et règles
- Un seul `requirements.txt` (dans `build/app/`).
- Dockerfile unique : `build/app/Dockerfile`.
- Tests exécutables : `python build/app/tests/main.py`.
- Respecter PEP8.
- Ne pas conserver markdowns inutiles (CONTRIBUTING/TODO/CHANGELOG) sauf s'ils sont activement maintenus.
- Conserver les dossiers de challenges s'ils existent.
- `.gitignore` présent et configuré (exclure artefacts, caches, virtualenvs, build, logs).

## CI/CD
- Le workflow `.github/workflows/docker-publish.yml` :
  - Installe dépendances depuis `build/app/requirements.txt`.
  - Exécute `python build/app/tests/main.py`.
  - Build et publie l'image uniquement si tous les tests passent avec succès.

## Nettoyage / maintenance
- Supprimer les fichiers redondants.
- Corriger les chemins dans Dockerfile/docker-compose après déplacement.
- Mettre à jour la documentation dans `README.md` (racine) et `build/deploy/README.md`.