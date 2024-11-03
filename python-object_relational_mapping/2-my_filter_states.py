#!/usr/bin/python3
"""
Get all rows of states table with name
matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY name = '{}' \
        ORDER BY states.id ASC;".format(sys.argv[4]))

    for state in cursor.fetchall():
        print("{}".format(state))

    cursor.close()
    db.close()
