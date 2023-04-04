import sqlite3
from pathlib import Path

class Connection:
    def __init__(self, conn):
        self.conn = conn
        pass

    # Create db file in data folder, if it doesn't exist
    def init_db(self):
        if Path.exists("./data/my_data.db") == False:
            Path('./data/my_data.db').touch()
            print("Created")
        else:
            print("Already created")
        return

    def connect(self):
        self.init_db()
        # Connect to database
        new_conn = sqlite3.connect("../data/my_db.db")
        conn = new_conn.cursor()
    #     conn.
    #
    # def disconnect(self):
    #     sqlite3.
    #     pass