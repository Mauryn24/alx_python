#!/usr/bin/python3

"""a script that lists all states from the database hbtn_0e_0_usa"""


import sys
import MySQLdb


if __name__ == "__main__":
    """connect to the MySQL database"""
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host="localhost",
                         port=3306)

    """create a cursor object"""
    cursor = db.cursor()

    """execute the SQL query"""
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    """Fetch all the rows"""
    results = cursor.fetchall()

    """print the results"""
    for row in results:
        print(row)

    """close the cursor object"""
    cursor.close()

    """close the connection to the database"""
    db.close()
