#!/usr/bin/python3
""" Free from SQL injection attacks """

import MySQLdb
import sys


if len(sys.argv) == 4:
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8"
            )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY\
            id ASC", (sys.argv[4],))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


def main():
    """ Empty function """

    ...

if __name__ == "__main__":
    main()
