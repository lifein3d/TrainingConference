"""
Name: Bryant Hanks
Assignment: CS336 Assignment #10
Created:12/10/2022
Description: Creates and populates DB table with passed through information
"""

import sqlite3

"""
Registrant class that sets attribute with for loop using a dictionary that is passed through
"""
class Registrant:
    def __init__(self, reg_dictionary):
        for key in reg_dictionary:
            setattr(self, key, reg_dictionary[key])

"""
Creates sqlite connection
"""
def connection():
    #creates the database with sqlite and creates a connection to use
    db_name = "conference.sqlite"
    conn = sqlite3.connect(db_name)
    return conn

"""
Creates SQL DB to store data from CSV
"""
def create_table(curs):

    curs.execute('CREATE TABLE IF NOT EXISTS registrants ( '
                 'registration_date text,' 
                 'title text, '
                 'firstname text, '
                 'lastname text , '
                 'addy1 text, '
                 'addy2 text, '
                 'city text, '
                 'state text, '
                 'zip integer, '
                 'telephone text, '
                 'email text, '
                 'position text, '
                 'company text, '
                 'day1 text, '
                 'day2 text, '
                 'day3 text);')


"""
insert class objects into DB table
@reg_list - list of objects which are individual registrants
"""
def insert_registrants(reg_list):

    conn = connection()
    curs = conn.cursor()

    create_table(curs)

    curs.execute("INSERT INTO registrants ("
                 "'registration_date',"
                 "'title',"
                 "'firstname',"
                 "'lastname',"
                 "'addy1',"
                 "'addy2',"
                 "'city',"
                 "'state',"
                 "'zip',"
                 "'telephone',"
                 "'email',"
                 "'position',"
                 "'company',"
                 "'day1',"
                 "'day2',"
                 "'day3'"
                 ") "
                 "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                 (reg_list))

    conn.commit()
    conn.close()