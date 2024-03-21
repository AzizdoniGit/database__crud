import sqlite3

conn = sqlite3.connect('tech.db')
cur = conn.cursor()
data = ('Ali Axmedov',)
sql = """Insert into user(data) values(?);"""
cur.execute(sql, data)
conn.commit()
conn.close()
print('Query executed successfully')


