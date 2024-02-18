#!/usr/bin/python3
import MySQLdb
import sys

cli = sys.argv


def connection():
    if len(cli) == 5:
        username, password, database, name = cli[1:]

        db = MySQLdb.connect(host='localhost', port=3306, user=username,
                             password=password, database=database)
        cur = db.cursor()
        cur.execute("""SELECT * FROM states
                    WHERE name='{}'
                    ORDER BY id""".format(name))
        user_select = cur.fetchone()
        if user_select:
            print(str(user_select))
        else:
            print(f"'{name}' not found in state")
    else:
        print("\n").join(["Add input value of the name of state to search for",
                          "Usage: <python script> username, password, database"
                          ])
        sys.exit(1)


if __name__ == "__main__":
    connection()
