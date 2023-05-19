"""
Name: Bryant Hanks
Assignment: CS336 Assignment #10
Created:12/11/2022
Description: Creates and populates DB table with CSV information
"""

import sqlite3, csv
from sqlite3 import Error

"""
Imports CSV data into table via a connection
@conn - connection to write to the database
"""
def importcsv(conn):
    curs = conn.cursor()

    file = open('database_code/awards.csv')
    next(file) #skip headers
    records = csv.reader(file)
    sql = "insert into nominees (name, description, image, votes)values (?,?,?,?)"

    curs.executemany(sql, records)

    conn.commit()
    conn.close()
    file.close()


"""
creates connection to the SQL database
"""
def db_connect():
    db_name = "conference.sqlite"
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except Error as e:
        print(e)
    return conn


"""
Creates SQL DB to store data from CSV
"""
def create():
    conn = db_connect()

    curs = conn.cursor()

    curs.execute('create table if not exists nominees ( '
                 'id integer primary key, '
                 'name text, '
                 'description text, '
                 'image text, '
                 'votes integer);')
    importcsv(conn)


if __name__ == '__main__':
    create()
