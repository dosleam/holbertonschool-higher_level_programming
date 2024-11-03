#!/usr/bin/python3
"""
Lists all cities where state name
from the database
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
    cursor.execute("SELECT cities.name \
                    FROM cities JOIN states ON cities.state_id = states.id \
                    WHERE states.name = %s \
                    ORDER BY cities.id ASC;", (sys.argv[4], ))

    print(", ".join([row[0] for row in cursor.fetchall()]))

    cursor.close()
    db.close()
