# Username Enumeration via Different Responses

## 🎯 Challenge Description
This is a vulnerable Flask application designed to demonstrate username enumeration attacks through different server responses.

## 🚀 Quick Start

### Pull and Run
```bash
docker pull cyberctf/username-enumeration-via-different-responses:latest
docker run -d -p 3206:3206 cyberctf/username-enumeration-via-different-responses:latest
```

### Access Application
- Open your browser to `http://localhost:3206`
- Try different usernames to observe response differences

### Docker Compose
```yaml
services:
  app:
    image: cyberctf/username-enumeration-via-different-responses:latest
    ports:
      - "3206:3206"
    restart: unless-stopped
```

## 🔧 Configuration
- **Port**: Application runs on port 3206 internally
- **Database**: SQLite in-memory (resets on restart)
- **Environment**: Production ready

## 📚 Learning Objectives
- Understand username enumeration vulnerabilities
- Learn to identify timing and response differences
- Practice reconnaissance techniques

## 🏷️ Tags
`cybersecurity` `ctf` `flask` `vulnerability` `enumeration` `python`

---
**CyberCTF** - Cybersecurity Training Platform

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