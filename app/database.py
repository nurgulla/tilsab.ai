import sqlite3
from flask import current_app

def get_db():
    db_path = current_app.config.get('DATABASE_URL', 'leads.db').replace('sqlite:///', '')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(app):
    db_path = app.config.get('DATABASE_URL', 'leads.db').replace('sqlite:///', '')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isim TEXT NOT NULL,
            email TEXT NOT NULL,
            ilgi_alani TEXT,
            amac TEXT,
            tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def lead_ekle(isim, email, ilgi_alani="", amac=""):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO leads (isim, email, ilgi_alani, amac) VALUES (?, ?, ?, ?)',
        (isim, email, ilgi_alani, amac)
    )
    conn.commit()
    conn.close()

def tum_leadler():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM leads ORDER BY tarih DESC')
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]
