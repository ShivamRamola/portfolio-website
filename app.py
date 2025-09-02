# app.py - Main Flask Application
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Database setup
def init_db():
    conn = sqlite3.connect('portfolio.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  email TEXT NOT NULL,
                  message TEXT NOT NULL,
                  date_created DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    projects = [
        {
            'name': 'Portfolio Website',
            'description': 'Personal portfolio built with Flask and SQLite',
            'tech': 'Python, Flask, SQLite, HTML, CSS',
            'github': '#'
        },
        {
            'name': 'Data Analysis Project',
            'description': 'Analyzed student performance data using Python',
            'tech': 'Python, Pandas, Matplotlib',
            'github': '#'
        }
    ]
    return render_template('projects.html', projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Save to database
        conn = sqlite3.connect('portfolio.db')
        c = conn.cursor()
        c.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
                  (name, email, message))
        conn.commit()
        conn.close()
        
        flash('Message sent successfully!', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/admin')
def admin():
    # View all messages (admin panel)
    conn = sqlite3.connect('portfolio.db')
    messages = conn.execute("SELECT * FROM contacts ORDER BY date_created DESC").fetchall()
    conn.close()
    
    return render_template('admin.html', messages=messages)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)