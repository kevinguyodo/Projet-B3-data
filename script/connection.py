import sqlite3
from pathlib import Path
import pandas as pd

class Connection:
    def __init__(self, conn):
        self.conn = conn
        pass

    # Create db file in data folder, if it doesn't exist
    def init_db(self):
        open("./data/clean_db.db", "w")
        open("./data/initial_db.db", "w")

    def connect(self):
        self.init_db()
        # Connect to database
        new_conn = sqlite3.connect("./data/clean_db.db")
        conn = new_conn.cursor()
        return conn, new_conn

    def get_data_from_csv(self):
        db_conn, db_new_conn = self.connect()
        users = pd.read_csv('./data/Drug_clean.csv', nrows=15)
        users.to_sql('drug', con=db_new_conn)
        my_data = db_new_conn.execute('''SELECT * FROM drug''').fetchall()
        print(my_data[1])
        # print(db_new_conn.execute('''SELECT * FROM drug''').fetchall())
        # print(users.head())

        # users.head()
    # def disconnect(self):
    #     sqlite3.
    #     pass