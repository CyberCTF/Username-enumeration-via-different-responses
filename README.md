# Employee Portal: Username Enumeration via Different Responses

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

**Difficulty:** 🟡 APPRENTICE | **Category:** Authentication | **Estimated Time:** 15-30 minutes

## 🎯 Challenge Overview

This lab demonstrates a vulnerability in an employee management portal where username enumeration is possible through different error responses. The application has predictable usernames and passwords that can be discovered through systematic testing.

## 🚀 Quick Start

### Using Docker
```bash
docker pull cyberctf/username-enumeration-via-different-responses:latest
docker run -d -p 3206:3206 cyberctf/username-enumeration-via-different-responses:latest
```

### Using Docker Compose
```bash
docker-compose up -d
```

**Access:** http://localhost:3206

## 📚 Learning Objectives

- ✅ Enumerate valid usernames by analyzing different error responses
- ✅ Brute force the password for the identified user  
- ✅ Access the employee dashboard to retrieve the flag

## 🛠️ Prerequisites

- Basic understanding of HTTP requests
- Familiarity with Burp Suite or similar tools
- Knowledge of authentication bypass techniques

## 🔧 Tools Recommended

- Burp Suite Community/Professional
- Web browser
- Wordlists for usernames and passwords

---

**🎓 CyberCTF** - Cybersecurity Training Platform
