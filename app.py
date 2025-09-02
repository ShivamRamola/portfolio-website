# app.py - Main Flask Application
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import os
import sqlite3

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-here')

class DatabaseError(Exception):
    pass

@app.errorhandler(DatabaseError)
def handle_database_error(e):
    return str(e), 500

@app.errorhandler(Exception)
def handle_error(e):
    return str(e), 500

def init_db():
    conn = sqlite3.connect('portfolio.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  email TEXT NOT NULL,
                  message TEXT NOT NULL,
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
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
            'github': 'https://github.com/ShivamRamola/portfolio-website',
            'Live': "https://portfolio-website-omega-weld-49.vercel.app/",
        },
        {
            'name': 'URL Shortener',
            'description': 'A simple URL shortener built with Flask',
            'tech': 'Python',
            'github': 'https://github.com/ShivamRamola/URL-Shortner',
            'Live': '#'
        },
        {
            'name': 'Banking System',
            'description': 'A console based banking system application',
            'tech': 'Python',
            'github': 'https://github.com/ShivamRamola/Banking-System',
            'Live': '#'
        },
        {
            'name': "Resume Screener",
            'description': 'A tool to screen resumes using NLP',
            'tech': 'Python, NLP',
            'github': 'https://github.com/ShivamRamola/Resume-Screener',
            'Live': '#'
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
    messages = conn.execute("SELECT * FROM contacts ORDER BY created_at DESC").fetchall()
    conn.close()
    
    return render_template('admin.html', messages=messages)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)