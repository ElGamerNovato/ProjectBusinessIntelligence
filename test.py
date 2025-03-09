import pymysql

pymysql.install_as_MySQLdb()

import MySQLdb
import os
from dotenv import load_dotenv

load_dotenv()

try:
    conn = MySQLdb.connect(
        host = os.getenv('DB_HOST'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD'),
        database = os.getenv('DB_NAME_ORIGEN')
    )
    cursor = conn.cursor()

    cursor.execute('show tables')

    tables = cursor.fetchall()
    print('Tables in the database:')
    for table in tables:
        print(table[0])

    cursor.close()
    conn.close()
except Exception as e:
    print(f'Hubo un error: {e}')