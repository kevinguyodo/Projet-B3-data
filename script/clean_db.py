import sqlite3
from pathlib import Path
import pandas as pd

class CleanDBConnection:
    def __init__(self):
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
        try:
            # Get database connection
            db_new_conn = self.connect()
            # Read CSV file, separate data to format their, and skip first rows => columns1, columns2 ...
            drug_data_csv = pd.read_csv('./data/Drug_clean.csv', sep=';', skiprows=[0])
            # Insert data in Database
            drug_data_csv.to_sql('cleandrug', con=db_new_conn, if_exists='replace')
            # First select request to prevent user
            all_data = db_new_conn.execute('''SELECT * FROM cleandrug''').fetchall()
            if all_data:
                print("Base de donnée 'cleandrug' créée, et donnée insérée")
            else:
                print("Base de donnée 'cleandrug' créée mais donnée non insérée")
        except:
            print("Quelque chose ne s'est passé comme prévu")