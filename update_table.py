import sqlite3

conn = sqlite3.connect('dashboard.db')
cur = conn.cursor()
sql = """
    UPDATE admins
    SET data = ?
    WHERE id = ?;
"""
cur.execute(sql, ('1312413312', 1))
cur.execute(sql, ('1425332523', 2))
cur.execute(sql, ('7556746534', 3))
cur.execute(sql, ('1208934792', 4))

conn.commit()
conn.close()
print('Query updated successfully')