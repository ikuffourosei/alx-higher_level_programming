#!/usr/bin/python3
import sys
import MySQLdb

cli = sys.argv


def connection():
    """Function that executes a query by filter names of state
    that begins with N
    """
    if len(cli) == 4:
        username, password, database = cli[1:]
        db = MySQLdb.connect(user=username, password=password,
                             database=database)
        cur = db.cursor()
        cur.execute("""SELECT * FROM states
                    WHERE name LIKE 'N%'
                    ORDER BY id""")
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
