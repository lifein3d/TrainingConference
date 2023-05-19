"""
Name: Bryant Hanks
Assignment: CS336 Assignment #10
Created:12/11/2022
Description: Creates and populates DB table with CSV information that is put into a dictionary
"""

import sqlite3, csv
from sqlite3 import Error


"""
Imports CSV data into table via a connection
@conn - connection to write to the database
"""
def importcsv(conn):
    curs = conn.cursor()

    fileName = 'database_code/workshops.csv'

    sql = 'insert into workshops (name, timeslot, room, start, end) values(?,?,?,?,?)'

    with open(fileName, 'r') as file:
        reader = csv.DictReader(file)
        values = [(i['name'], i['timeslot'], i['room'], i['start'], i['end']) for i in reader]
    curs.executemany(sql, values)

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

    curs.execute('create table if not exists workshops ( '
                 'name text, '
                 'timeslot integer, '
                 'room text, '
                 'start time, '
                 'end time);')
    importcsv(conn)


if __name__ == '__main__':
    create()
