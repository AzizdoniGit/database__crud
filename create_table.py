import sqlite3

conn = sqlite3.connect('tech.db')
cur = conn.cursor()
sql = """
    CREATE TABLE IF NOT Exists user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT
    );
"""
cur.execute(sql)
conn.commit()
conn.close()