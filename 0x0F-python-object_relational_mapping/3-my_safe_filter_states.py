#!/usr/bin/python3
"""a script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
But this time, write one that is safe from MySQL injections!
"""


import MySQLdb
import sys


def connection():
    """Displays all query results according to user input, safe from sql
    injections
    """
    cli = sys.argv
    if len(cli) == 5:
        username, password, database, name = cli[1:]

        db = MySQLdb.connect(port=3306, user=username, host='localhost',
                             password=password, database=database)
        cur = db.cursor()

        # executing using safe query parameter
        cur.execute("""SELECT * FROM states
                    WHERE name LIKE %(name)s
                    ORDER BY id ASC""", {'name': name})
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
