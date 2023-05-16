from script.clean_db import CleanDBConnection
from script.initial_db import InitialDBConnection

def main():
    clean_db_conn = CleanDBConnection()
    clean_db_conn.get_data_from_csv()

    initial_db_conn = InitialDBConnection()
    initial_db_conn.get_data_from_csv()

main()
