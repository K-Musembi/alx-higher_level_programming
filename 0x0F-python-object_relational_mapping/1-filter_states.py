#!/usr/bin/python3
'''List all states starting with N'''

import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]

conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name)

cur = conn.cursor()

cur.execute("SELECT * FROM states WHERE name RLIKE '^[N]' ORDER BY id")

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()


def main():
    '''empty function'''

    pass


if __name__ == "__main__":
    main()
