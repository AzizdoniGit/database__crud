import sqlite3

conn = sqlite3.connect('shop.db')
cur = conn.cursor()
sql = "SELECT * FROM orders;"
cur.execute(sql)
# rows = cur.fetchall()
# print(rows)
# for i in cur.fetchall():
#     print(i)
conn.close()