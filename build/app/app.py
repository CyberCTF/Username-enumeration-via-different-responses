from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'employee_portal_secret_key_2024'
app.config['DATABASE'] = 'employees.db'

def init_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            full_name TEXT NOT NULL,
            department TEXT NOT NULL,
            email TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Remove old admin user if exists
    cursor.execute('DELETE FROM employees WHERE username = ?', ('admin',))
    
    # Force reset - delete all existing employees and recreate with new passwords
    cursor.execute('DELETE FROM employees')
    
    # Insert default employees with predictable credentials
    # Note: All usernames have same length (8 chars) except administrator (13 chars) for enumeration
    employees = [
        ('administrator', 'password1', 'System Administrator', 'IT', 'administrator@company.com'),
        ('johndoe1', 'password123', 'John Doe', 'Engineering', 'john.doe@company.com'),
        ('janesmith', 'welcome2024', 'Jane Smith', 'Marketing', 'jane.smith@company.com'),
        ('mikewils', 'securepass', 'Mike Wilson', 'Sales', 'mike.wilson@company.com'),
        ('sarahjns', 'user123', 'Sarah Jones', 'HR', 'sarah.jones@company.com'),
        ('davidbrn', 'david2024', 'David Brown', 'Finance', 'david.brown@company.com'),
        ('lisagrc1', 'lisa123', 'Lisa Garcia', 'Operations', 'lisa.garcia@company.com'),
        ('robertle', 'robertlee', 'Robert Lee', 'Legal', 'robert.lee@company.com'),
        ('emmadv1s', 'emma2024', 'Emma Davis', 'Customer Support', 'emma.davis@company.com'),
        ('thomasan', 'thomas123', 'Thomas Anderson', 'Product', 'thomas.anderson@company.com')
    ]
    
    for employee in employees:
        try:
            cursor.execute('''
                INSERT OR IGNORE INTO employees (username, password, full_name, department, email)
                VALUES (?, ?, ?, ?, ?)
            ''', employee)
        except:
            pass
    
    conn.commit()
    conn.close()

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/employees-directory')
def employees_directory():
    """Public employees directory - no login required"""
    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    cursor.execute('''
        SELECT username, full_name, department, email, created_at 
        FROM employees 
        ORDER BY department, full_name
    ''')
    employees_list = cursor.fetchall()
    conn.close()
    
    return render_template('employees_directory.html', employees=employees_list)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', '').strip()
    password = request.form.get('password', '').strip()
    
    if not username or not password:
        flash('Please provide both username and password', 'error')
        return render_template('login.html')
    
    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    
    # Check if username exists first
    cursor.execute('SELECT id, username, password, full_name FROM employees WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    
    if not user:
        # Username doesn't exist - standard response length
        # All invalid usernames get same response except 'administrator'
        if username == 'administrator':
            # Special response for administrator (different length for enumeration)
            flash('Invalid username or password. Access denied.', 'error')
        else:
            # Standard response for all other invalid usernames
            flash('Invalid username or password', 'error')
        return render_template('login.html')
    
    if user[2] != password:
        # Username exists but password is wrong - same length as valid username error
        if username == 'administrator':
            # Same length as above for administrator
            flash('Invalid username or password. Access denied.', 'error')
        else:
            # Standard response for valid usernames with wrong password
            flash('Invalid username or password', 'error')
        return render_template('login.html')
    
    # Login successful
    session['user_id'] = user[0]
    session['username'] = user[1]
    session['full_name'] = user[3]
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('index'))
    
    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    cursor.execute('''
        SELECT username, full_name, department, email, created_at 
        FROM employees WHERE id = ?
    ''', (session['user_id'],))
    user_data = cursor.fetchone()
    conn.close()
    
    if not user_data:
        session.clear()
        return redirect(url_for('index'))
    
    # Show password instead of obvious flag
    admin_password = "password1"
    
    return render_template('dashboard.html', 
                         user_data=user_data, 
                         admin_password=admin_password,
                         full_name=session['full_name'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/credentials')
def credentials():
    return render_template('credentials.html')

@app.route('/employees')
def employees():
    if 'user_id' not in session:
        return redirect(url_for('index'))
    
    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    cursor.execute('''
        SELECT username, full_name, department, email, created_at 
        FROM employees 
        ORDER BY created_at DESC
    ''')
    employees_list = cursor.fetchall()
    conn.close()
    
    return render_template('employees.html', employees=employees_list)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=3206, debug=False)
