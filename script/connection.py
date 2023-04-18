import sqlite3
from pathlib import Path
import panda

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
        print("Connect data")


    # def disconnect(self):
    #     sqlite3.
    #     pass