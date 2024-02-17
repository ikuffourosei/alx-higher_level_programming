#!/usr/bin/python3
import MySQLdb
import sys

cli = sys.argv


def connection():
    if len(cli) == 5:
        username, password, database, name = cli[1:]

        db = MySQLdb.connect(user=username, password=password,
                             database=database)
        cur = db.cursor()
        cur.execute("""SELECT * FROM states
                    WHERE name=%s
                    ORDER BY id""", (name,))
        user_select = cur.fetchone()
        print(str(user_select))
    else:
        print("\n").join(["Add input value of the name of state to search for",
                          "Usage: <python script> username, password, database"
                          ])
        sys.exit(1)


if __name__ == "__main__":
    connection()
