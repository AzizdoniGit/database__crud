import sqlite3

conn = sqlite3.connect('dashboard.db')
cur = conn.cursor()
sql = """
    DELETE FROM admins WHERE id = ?;
    
"""
cur.execute(sql, (1,))

conn.commit()
conn.close()
print('Query removed successfully')