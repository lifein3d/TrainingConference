"""
Name: Bryant Hanks
Assignment: CS336 Assignment #10
Created:12/11/2022
Description: Creates and populates DB table
"""

import sqlite3,csv
from sqlite3 import Error


"""
Imports CSV data into table via a connection
@conn - connection to write to the database
"""
def importcsv(conn):
    curs = conn.cursor()

    file = open('database_code/users.csv')
    next(file) #skip headers
    records = csv.reader(file)
    sql = "insert into users (username, firstname, lastname, password)values (?,?,?,?)"

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

    curs.execute('create table if not exists users ( '
                 'id integer primary key, '
                 'username text, '
                 'firstname text, '
                 'lastname text, '
                 'password text);')
    importcsv(conn)

"""
Validates that the provided username and password are in the user database
"""
def validate(username, password):
    connection = db_connect()
    cursor = connection.cursor()
    cursor.execute('select username, password from users where username = ? and password = ?', (username, password))
    return cursor.fetchone()

if __name__ == '__main__':
    create()
