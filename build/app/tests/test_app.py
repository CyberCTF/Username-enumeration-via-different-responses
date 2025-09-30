import pytest
import requests
import sqlite3
import os
import tempfile
from unittest.mock import patch
import sys
import os

# Add the app directory to the path
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    app.config['DATABASE'] = ':memory:'  # Use in-memory database for testing
    
    with app.test_client() as client:
        with app.app_context():
            # Initialize the database
            from app import init_db
            init_db()  # This will create tables and populate with employees
            
            yield client

def test_index_page(client):
    """Test that the index page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Employee Portal' in response.data
    assert b'Sign in' in response.data

def test_login_invalid_username(client):
    """Test login with invalid username returns 'Invalid username or password' error."""
    response = client.post('/login', data={
        'username': 'nonexistent',
        'password': 'anypassword'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Invalid username or password' in response.data

def test_login_valid_username_wrong_password(client):
    """Test login with valid username but wrong password returns 'Invalid username or password. Please try again.' error."""
    response = client.post('/login', data={
        'username': 'administrator',
        'password': 'wrongpassword'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Invalid username or password. Please try again.' in response.data

def test_login_valid_credentials(client):
    """Test successful login with valid credentials."""
    response = client.post('/login', data={
        'username': 'administrator',
        'password': 'password1'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Welcome back' in response.data
    assert b'password1' in response.data

def test_dashboard_access_without_login(client):
    """Test that dashboard redirects to login when not authenticated."""
    response = client.get('/dashboard', follow_redirects=True)
    assert response.status_code == 200
    assert b'Employee Portal' in response.data
    assert b'Sign in' in response.data

def test_employees_page_access_without_login(client):
    """Test that employees page redirects to login when not authenticated."""
    response = client.get('/employees', follow_redirects=True)
    assert response.status_code == 200
    assert b'Employee Portal' in response.data
    assert b'Sign in' in response.data

def test_employees_page_with_login(client):
    """Test employees page access after successful login."""
    # First login
    client.post('/login', data={
        'username': 'administrator',
        'password': 'password1'
    })
    
    # Then access employees page
    response = client.get('/employees')
    assert response.status_code == 200
    assert b'Employee Directory' in response.data
    assert b'administrator' in response.data
    assert b'johndoe1' in response.data
    assert b'janesmith' in response.data

def test_logout(client):
    """Test logout functionality."""
    # First login
    client.post('/login', data={
        'username': 'administrator',
        'password': 'password1'
    })
    
    # Then logout
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Employee Portal' in response.data
    assert b'Sign in' in response.data

def test_username_enumeration_vulnerability(client):
    """Test the username enumeration vulnerability by checking different error messages."""
    # Test with non-existent username
    response1 = client.post('/login', data={
        'username': 'nonexistent',
        'password': 'anypassword'
    }, follow_redirects=True)
    
    # Test with valid username but wrong password
    response2 = client.post('/login', data={
        'username': 'administrator',
        'password': 'wrongpassword'
    }, follow_redirects=True)
    
    # The responses should be different
    assert b'Invalid username or password' in response1.data
    assert b'Invalid username or password. Please try again.' in response2.data
    assert b'Invalid username or password. Please try again.' not in response1.data

def test_all_valid_usernames(client):
    """Test that all predefined usernames are valid and return 'Invalid username or password. Please try again.' with wrong password."""
    valid_usernames = ['administrator', 'johndoe1', 'janesmith', 'mikewils', 'sarahjns']
    
    for username in valid_usernames:
        response = client.post('/login', data={
            'username': username,
            'password': 'wrongpassword'
        }, follow_redirects=True)
        
        assert response.status_code == 200
        assert b'Invalid username or password. Please try again.' in response.data
        assert b'Invalid username or password' not in response.data

def test_flag_retrieval(client):
    """Test that the flag is accessible after successful login."""
    response = client.post('/login', data={
        'username': 'administrator',
        'password': 'password1'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'password1' in response.data

def test_multiple_user_logins(client):
    """Test that different users can log in and see their respective data."""
    test_users = [
        ('administrator', 'password1', 'System Administrator'),
        ('johndoe1', 'password123', 'John Doe'),
        ('janesmith', 'welcome2024', 'Jane Smith')
    ]
    
    for username, password, full_name in test_users:
        response = client.post('/login', data={
            'username': username,
            'password': password
        }, follow_redirects=True)
        
        assert response.status_code == 200
        assert full_name.encode() in response.data
        assert b'password1' in response.data
        
        # Logout before next test
        client.get('/logout')

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
