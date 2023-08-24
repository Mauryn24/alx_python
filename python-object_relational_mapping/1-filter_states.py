#!/usr/bin/python3

"""lists all states with names starting with N """


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

    """Execute a query"""
    cursor.execute("SELECT * FROM states\
                   WHERE name LIKE BINARY 'N%'\
                   ORDER BY id ASC")

    """Fetch all rows with matching query"""
    data = cursor.fetchall()

    """display results"""
    for row in data:
        print(row)

    """close the cursor"""
    cursor.close()

    """close the db connection"""
    db.close()
