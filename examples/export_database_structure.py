#!/usr/bin/env python3
import mysql.connector
import csv
import getpass
import argparse

parser = argparse.ArgumentParser(description='Export MySQL database tables and columns information to CSV.')
parser.add_argument('-host', type=str, help='Database host', default='localhost')
parser.add_argument('-port', type=int, help='Database port', default=3306)
parser.add_argument('-user', type=str, help='Username for MySQL', required=True)
parser.add_argument('-database', type=str, help='Database name', required=True)

args = parser.parse_args()
password = getpass.getpass('Enter your MySQL password: ')

def connect_to_db(host, port, user, passwd, db):
    return mysql.connector.connect(host=host, port=port, user=user, passwd=passwd, database=db)

def fetch_data(cursor):
    query = ("SELECT TABLE_NAME, COLUMN_NAME, COLUMN_COMMENT FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = %s ORDER BY TABLE_NAME, ORDINAL_POSITION")
    cursor.execute(query, (args.database,))

    with open('database_structure.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Table Name', 'Column Name', 'Column Comment'])
        for (table_name, column_name, column_comment) in cursor:
            writer.writerow([table_name, column_name, column_comment])
def main():
    try:
        cnx = connect_to_db(args.host, args.port, args.user, password, args.database)
        cursor = cnx.cursor()
        fetch_data(cursor)
    finally:
        cursor.close()
        cnx.close()

if __name__ == '__main__':
    main()
