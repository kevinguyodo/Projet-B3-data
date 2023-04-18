import sqlite3
from pathlib import Path
import pandas as pd

class CleanDBConnection:
    def __init__(self, conn):
        self.conn = conn
        pass

    # Create db file in data folder, if it doesn't exist
    def init_db(self):
        open("./data/clean_db.db", "w")

    def connect(self):
        self.init_db()
        # Connect to database
        new_conn = sqlite3.connect("./data/clean_db.db")
        return new_conn

    def get_data_from_csv(self):
        # Get database connection
        db_new_conn = self.connect()
        # Read CSV file, separate data to format their, and skip first rows => columns1, columns2 ...
        drug_data_csv = pd.read_csv('./data/Drug_clean.csv', sep = ';', skiprows=[0])
        # Insert data in Database
        drug_data_csv.to_sql('cleandrug', con=db_new_conn, if_exists= 'append')
        # First select request
        all_data = db_new_conn.execute('''SELECT * FROM cleandrug''').fetchall()
        print(all_data)

    def get_description(self):
        init_db_data = self.connect()
        init_db_description = init_db_data.execute('''SELECT Description FROM cleandrug WHERE Description IS NOT NULL''').fetchall()
        print(init_db_description)
        pass
