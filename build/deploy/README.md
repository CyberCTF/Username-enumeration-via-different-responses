# Deployment and Development Guide

## Development Environment

### Local Development with Docker Compose

1. **Development mode** (avec hot-reload):
```bash
cd build/deploy
docker-compose -f docker-compose.dev.yml up --build
```

L'application sera accessible sur http://localhost:3206

### Production Deployment

Pour déployer en production, utilisez le docker-compose.yml à la racine :

```bash
# À la racine du projet
docker-compose up --build -d
```

## Structure du Projet

```
build/
├── app/                    # Code applicatif
│   ├── Dockerfile         # Container de l'app
│   ├── app.py            # Point d'entrée Flask
│   ├── requirements.txt  # Dépendances Python
│   ├── templates/        # Templates HTML
│   └── tests/           # Tests unitaires
└── deploy/              # Configuration déploiement
    ├── docker-compose.dev.yml  # Configuration développement
    └── README.md               # Ce fichier
```

## Tests

Exécuter les tests :
```bash
python build/app/tests/main.py
```

## Configuration

### Variables d'environnement

- `FLASK_ENV`: `development` ou `production`
- `FLASK_DEBUG`: `1` pour le debug mode
- `FLASK_APP`: `app.py`

### Ports

- **Development**: 3206 → 5000 (container)
- **Production**: 3206 → 5000 (container)

## Troubleshooting

1. **Problème de permissions**: Vérifier que Docker a accès aux volumes
2. **Port occupé**: Changer le port dans docker-compose.yml  
3. **Build échoue**: Vérifier les dépendances dans requirements.txt