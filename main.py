from script.clean_db import CleanDBConnection
from script.initial_db import InitialDBConnection


def main():
    # clean_db_conn = CleanDBConnection("Hello World")
    # clean_db_conn.get_data_from_csv()

    initial_db_conn = InitialDBConnection()
    initial_db_conn.get_data_from_csv()
    # initial_db_conn.get_description()
    # new_conn.get_description()

main()