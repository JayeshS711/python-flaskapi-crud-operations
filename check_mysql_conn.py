import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='jsdb',
                                       user='root',
                                       password='Victor@7111997')
        if conn.is_connected():
            print('Connected to MySQL database')
        cursor=conn.cursor()
        cursor.execute("Show tables")
        for table_name in cursor:
            print(table_name)

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    connect()