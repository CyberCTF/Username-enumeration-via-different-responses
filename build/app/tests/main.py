#!/usr/bin/env python3
"""
Simplified test runner for the Employee Portal application.
Execute with: python build/app/tests/main.py
"""
import os
import sys

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
    
    # Test 3: Basic Flask routes
    try:
        with app.test_client() as client:
            # Test login page
            response = client.get('/')
            if response.status_code == 200:
                print("✓ Login page accessible")
            else:
                print(f"✗ Login page returned status {response.status_code}")
                return False
                
    except Exception as e:
        print(f"✗ Route testing failed: {e}")
        return False
    
    # Test 4: Template rendering
    try:
        with app.app_context():
            from flask import render_template_string
            test_template = render_template_string("<h1>Test</h1>")
            if test_template:
                print("✓ Template engine working")
            else:
                print("✗ Template engine failed")
                return False
                
    except Exception as e:
        print(f"✗ Template test failed: {e}")
        return False

    print(f"\n=== ALL BASIC TESTS COMPLETED SUCCESSFULLY ===")
    return True

def main():
    """Main test runner."""
    print("Employee Portal Test Suite")
    print("=" * 50)
    
    # Run basic tests
    basic_success = run_basic_tests()
    
    # Final result
    if basic_success:
        print("\n🎉 ALL TESTS PASSED!")
        print("Infrastructure is working correctly.")
        print("Note: Advanced tests may require additional setup.")
        sys.exit(0)
    else:
        print("\n❌ BASIC TESTS FAILED!")
        sys.exit(1)

if __name__ == "__main__":
    main()