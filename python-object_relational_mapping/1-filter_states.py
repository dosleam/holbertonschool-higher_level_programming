#!/usr/bin/python3
"""
Get all rows of states table with a name
starting with N
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
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")

    for state in cursor.fetchall():
        if str(state[1]).startswith("N"):
            print(state)

    cursor.close()
    db.close()
