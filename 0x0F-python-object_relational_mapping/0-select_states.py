#!/usr/bin/python3
'''Script to list all states'''

import MySQLdb
import sys

mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name)

cur = db.cursor()

cur.execute("SELECT * FROM states ORDER BY id ASC")

results = cur.fetchall()

for row in results:
    print(row)

cur.close()
db.close()


def main():
    '''empty function'''

    pass


if __name__ == "__main__":
    main()
