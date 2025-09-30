{
  "lab_readme": {
    "title": "Employee Portal: Username Enumeration via Different Responses",
    "difficulty": "APPRENTICE",
    "category": "Authentication",
    "description": "This lab demonstrates a vulnerability in an employee management portal where username enumeration is possible through different error responses. The application has predictable usernames and passwords that can be discovered through systematic testing.",
    "objectives": [
      "Enumerate valid usernames by analyzing different error responses",
      "Brute force the password for the identified user",
      "Access the employee dashboard to retrieve the flag"
    ],
    "prerequisites": [
      "Basic understanding of HTTP requests",
      "Familiarity with Burp Suite or similar tools",
      "Knowledge of authentication bypass techniques"
    ],
    "tools": [
      "Burp Suite Community/Professional",
      "Web browser",
      "Wordlists for usernames and passwords"
    ],
    "setup": "Run `docker-compose up -d` in the deploy directory to start the application on port 3206",
    "access": "http://localhost:3206",
    "flag_format": "SecurePass2024!",
    "estimated_time": "15-30 minutes"
  }
}
