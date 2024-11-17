import sqlite3

DB_PATH = 'evaluation.db'

def create_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS responses (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 student_id TEXT,
                 answer_text TEXT,
                 score INTEGER
                 )''')
    conn.commit()
    conn.close()

def insert_response(student_id, answer_text, score):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO responses (student_id, answer_text, score) VALUES (?, ?, ?)",
              (student_id, answer_text, score))
    conn.commit()
    conn.close()
