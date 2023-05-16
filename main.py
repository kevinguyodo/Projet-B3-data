from script.clean_db import CleanDBConnection
from script.initial_db import InitialDBConnection
from script.final_db import FinalDBConnection
import os

def main():
    clean_db_conn = CleanDBConnection()
    clean_db_conn.get_data_from_csv()

    initial_db_conn = InitialDBConnection()
    initial_db_conn.get_data_from_csv()

    if os.path.exists("data/final_drug.csv"):
        final_db_conn = FinalDBConnection()
        final_db_conn.get_data_from_csv()

main()