#!\usr\bin\python3

"""
a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time,
write one that is safe from MySQL injections!
"""

import sys
import MySQLdb

if __name__ == '__main__':
    """connect to mysql server"""
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host="localhost",
                         port=3306)

    """create a cursor"""
    cursor = db.cursor()

    """execute a query"""
    cursor.execute("SELECT * FROM states WHERE name LIKE\
               BINARY %(name)s ORDER BY\
               id ASC", {'name': sys.argv[4]})
    
    """fetch data"""
    data = cursor.fetchall()

    """print results"""
    for row in data:
        print(row)

    """close cursor"""
    cursor.close()

    """close sql connection"""
    db.close()