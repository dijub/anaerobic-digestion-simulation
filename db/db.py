import sqlite3 
import csv 

class Database:
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        columns_str = ', '.join(columns)
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})"
        self.cursor.execute(query)
        self.conn.commit()
        
    def delete_table(self, table_name):
        query = f'DROP TABLE IF EXISTS {table_name}'
        self.cursor.execute(query)
        self.conn.commit()

    def insert_data(self, table_name, data_list):
        placeholders = ', '.join(['?' for _ in range(len(data_list[0]))])
        query = f"INSERT INTO {table_name} (name, formula, cas_number, type, weight_molar) VALUES ({placeholders})"
        self.cursor.executemany(query, data_list)
        self.conn.commit()

    def get_data(self, table_name, condition=None):
        if condition:
            query = f"SELECT * FROM {table_name} WHERE {condition}"
        else:
            query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update_data(self, table_name, data, condition):
        update_values = ', '.join([f"{key} = ?" for key in data.keys()])
        query = f"UPDATE {table_name} SET {update_values} WHERE {condition}"
        self.cursor.execute(query, tuple(data.values()))
        self.conn.commit()

    def delete_data(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.cursor.execute(query)
        self.conn.commit()

    def close(self):
        self.conn.close()
        
def read_csv(file):
    data = []
    with open(file, 'r')as f:
        csv_reader = csv.reader(f, delimiter=';')
        for line in csv_reader:
            if 'formula' in line:
                continue
            data.append(tuple(line))
            
    return data
            
if __name__ == '__main__':
    db = Database('db/db.db')
    columns = [
        'id INTEGER PRIMARY KEY AUTOINCREMENT',
        'name TEXT',
        'formula TEXT',
        'cas_number TEXT',
        'type TEXT',
        'weight_molar REAL'
    ]
    db.delete_table('compounds')    
    db.create_table('compounds', columns)
    
    data = read_csv('db/compounds.csv')
    
    db.insert_data('compounds', data)
    
    print(db.get_data('compounds'))