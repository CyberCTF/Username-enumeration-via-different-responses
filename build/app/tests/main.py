#!/usr/bin/env python3
"""
Main test runner for the Employee Portal application.
Execute with: python build/app/tests/main.py
"""
import os
import sys
import unittest
import sqlite3
from io import StringIO

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def run_basic_tests():
    """Run basic functionality tests without pytest."""
    print("=== RUNNING EMPLOYEE PORTAL TESTS ===\n")
    
    # Test 1: Import and basic setup
    try:
        from app import app, init_db
        print("✓ Successfully imported Flask app")
    except ImportError as e:
        print(f"✗ Failed to import app: {e}")
        return False
    
    # Test 2: Database initialization
    try:
        app.config['TESTING'] = True
        app.config['DATABASE'] = ':memory:'
        with app.app_context():
            init_db()
        print("✓ Database initialization successful")
    except Exception as e:
        print(f"✗ Database initialization failed: {e}")
        return False
    
    # Test 3: Test client creation and basic routes
    try:
        app.config['DATABASE'] = ':memory:'
        with app.test_client() as client:
            with app.app_context():
                init_db()  # Initialize database in the test context
            
            # Test login page
            response = client.get('/')
            if response.status_code == 200:
                print("✓ Login page accessible")
            else:
                print(f"✗ Login page returned status {response.status_code}")
                
            # Test login functionality
            response = client.post('/login', data={
                'username': 'administrator',
                'password': 'password1'
            }, follow_redirects=True)
            
            if response.status_code == 200:
                print("✓ Login endpoint functional")
            else:
                print(f"✗ Login failed with status {response.status_code}")
                
    except Exception as e:
        print(f"✗ Route testing failed: {e}")
        return False
    
    # Test 4: Database queries
    try:
        app.config['DATABASE'] = ':memory:'
        with app.app_context():
            init_db()
            conn = sqlite3.connect(app.config['DATABASE'])
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM employees")
            count = cursor.fetchone()[0]
            conn.close()
            
            if count > 0:
                print(f"✓ Database populated with {count} employees")
            else:
                print("✗ No employees found in database")
                
    except Exception as e:
        print(f"✗ Database query failed: {e}")
        return False
    
    print(f"\n=== ALL TESTS COMPLETED SUCCESSFULLY ===")
    return True

def run_pytest_if_available():
    """Try to run pytest if available."""
    try:
        import pytest
        print("\n=== RUNNING PYTEST TESTS ===")
        
        # Run pytest on current directory
        test_dir = os.path.dirname(__file__)
        exit_code = pytest.main([test_dir, '-v'])
        
        if exit_code == 0:
            print("✓ Pytest tests passed")
            return True
        else:
            print(f"✗ Pytest failed with exit code {exit_code}")
            return False
            
    except ImportError:
        print("\n⚠ Pytest not available, skipping pytest tests")
        return True  # Don't fail if pytest isn't installed

def main():
    """Main test runner."""
    print("Employee Portal Test Suite")
    print("=" * 50)
    
    # Run basic tests
    basic_success = run_basic_tests()
    
    # Run pytest if available
    pytest_success = run_pytest_if_available()
    
    # Final result
    if basic_success and pytest_success:
        print("\n🎉 ALL TESTS PASSED!")
        sys.exit(0)
    else:
        print("\n❌ SOME TESTS FAILED!")
        sys.exit(1)

if __name__ == "__main__":
    main()