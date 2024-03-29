#!/usr/bin/python3
""" List all cities of a state
"""

import MySQLdb
import sys


if len(sys.argv) == 5:
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT cities.name FROM cities JOIN states ON\
            cities.state_id = states.id WHERE states.name = %s ORDER BY\
            cities.id ASC", (sys.argv[4],))

    rows = cursor.fetchall()
    print(",".join([row[0] for row in rows]))

    cursor.close()
    db.close()


def main():
    """ Empty function """

    ...

if __name__ == "__main__":
    main()
