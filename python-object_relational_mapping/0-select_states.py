#!/usr/bin/python3

"""a script that lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

def main(username, password, database):
    #connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    
    #create a cursor object
    cursor = db.cursor()

    #execute the SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    #Fetch all the rows
    results = cursor.fetchall()

    #print the results
    for row in results:
        print(row[0], row[1])
    
    #close the cursor object
    cursor.close()

    #close the connection to the database
    db.close

"""Code here will only run if this script is the main program It won't run if this script is imported as a module"""

if __name__ == "main":
    #get the username, password and databasenamr from the commandline arguement
    username = input("Enter MySQl username: ")
    password = input("Enter MySQL password: ")
    database = input("Enter MySQL database name: ")

    #call the main function
    main(username, password, database)