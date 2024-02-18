#!/usr/bin/python3
""" a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
"""


import MySQLdb
import sys


def connection():
    """Function that displays the result of a query where query is user input
    """
    cli = sys.argv
    if len(cli) == 5:
        username, password, database, name = cli[1:]

        db = MySQLdb.connect(port=3306, user=username, host='localhost',
                             password=password, database=database)
        cur = db.cursor()
        cur.execute("""SELECT * FROM states WHERE name LIKE
                    '{:s}' ORDER BY id ASC""".format(name))
        user_select = cur.fetchall()
        if user_select:
            print(user_select[0])
        else:
            print(f"'{name}' not found in state")
    else:
        print("\n").join(["Add input value of the name of state to search for",
                          "Usage: <python script> username, password, database"
                          ])
        sys.exit(1)


if __name__ == "__main__":
    connection()
