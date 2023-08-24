#!/usr/bin/python3

"""
Takes arguements and displays all values
in the states table where name matches the arguement
"""

import sys
import MySQLdb

if __name__ == '__main__':
    """connect to the MySQL server"""
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    """create a cursor object"""
    cursor = db.cursor()

    """execute the query"""
    cursor.execute("SELECT * FROM states\
        WHERE name LIKE BINARY '{}'\
        ORDER BR id ASC".format(sys.argv[4]))

    """fetch the data"""
    data = cursor.fetchall()

    """print the results"""
    for row in data:
        print(row)

    """close the cursor"""
    cursor.close()

    """close the connection"""
    db.close()