from script.connection import Connection



def main():
    new_conn= Connection("Hello World")
    new_conn.get_data_from_csv()


main()