#!/usr/bin/python3

"""script that lists all cities from the database hbtn_0e_4_usa"""


import sys
import MySQLdb


if __name__ == "__main__":
    """connect to sql server"""
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host="localhost",
                         port=3306)

    """create a cursor object"""
    cursor = db.cursor()

    """execute the query"""
    cursor.execute("SELECT c.id, c.name, s.name\
                   FROM states s, cities c\
                   WHERE c.state_id = s.id\
                   ORDER BY c.id ASC")

    """fetch the data"""
    data = cursor.fetchall()

    """display the results"""
    for row in data:
        print(row)

    """close the cursor"""
    cursor.close()

    """close the connection"""
    db.close()
