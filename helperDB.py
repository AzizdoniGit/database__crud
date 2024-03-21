import sqlite3


class helperDB:
    def __init__(self, dbname: str = 'tech.db'):
        self.conn = sqlite3.connect(dbname)
        self.cur = self.conn.cursor()
        self.table_name = ''

    def setup(self, table_name: str = 'customer'):
        self.table_name = table_name
        sql = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT
            );"""
        self.cur.execute(sql)
        self.conn.commit()

    def add_item(self, data: str):
        sql = f"""INSERT INTO {self.table_name} (data) VALUES (?)"""
        self.cur.execute(sql, (data,))
        self.conn.commit()

    def get_item(self):
        sql = f"SELECT * FROM {self.table_name};"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        return rows

    def update_item(self, old_data: str, new_data: str):
        sql = f"""
            UPDATE {self.table_name}
            SET data = ?
            WHERE data = ?;
        """
        self.cur.execute(sql, (new_data, old_data))
        self.conn.commit()

    def remove_item(self, id: int):
        sql = f"""
            DELETE FROM {self.table_name} WHERE id = ?;

        """
        self.cur.execute(sql, (id,))

        self.conn.commit()
        print('Query removed successfully')

    def close_db(self):
        self.conn.close()

shop = helperDB('shop.db')

shop.setup('customer')

shop.add_item('234')
shop.add_item('124')

shop.remove_item(2)
print('Query removed successfully')

shop.update_item('234', '567')
print('Query updated successfully')

print(shop.get_item())

shop.setup('orders')
shop.add_item('42565437')
shop.add_item('76354723')
print(shop.get_item())

dashboard = helperDB('dashboard.db')
dashboard.setup('admins')
dashboard.add_item('234234324')
dashboard.add_item('546345235')
print(dashboard.get_item())
print('Query executed successfully')