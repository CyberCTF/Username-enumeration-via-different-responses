# Username Enumeration via Different Responses

## Scenario
Vulnerability lab demonstrating a critical flaw in an employee management portal authentication system. The application reveals different error messages for valid vs invalid usernames, allowing attackers to enumerate valid accounts and subsequently brute force passwords.

## How to run
```bash
git clone https://github.com/CyberCTF/Username-enumeration-via-different-responses.git
cd Username-enumeration-via-different-responses
docker compose -f build/deploy/docker-compose.dev.yml up -d --build
```
**Access:** http://localhost:3206
