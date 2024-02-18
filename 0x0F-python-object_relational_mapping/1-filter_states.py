#!/usr/bin/python3
'''a script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa:
'''

import sys
import MySQLdb


def connection():
    """Function that executes a query by filter names of state
    that begins with 'N'
    """
    cli = sys.argv
    if len(cli) == 4:
        username, password, database = cli[1:]
        db = MySQLdb.connect(host='localhost', port=3306, user=username,
                             password=password, database=database)
        cur = db.cursor()
        cur.execute("""SELECT * FROM states
                    WHERE name LIKE 'N%'
                    ORDER BY id ASC""")
        names = cur.fetchall()
        for items in names:
            print(str(items))

        # cleaning up
        cur.close()
        db.close()
    else:
        print(f"Usage: <python script> username, password, database")
        sys.exit(1)


if __name__ == "__main__":
    connection()
