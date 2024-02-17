#!/usr/bin/python3
import MySQLdb
import sys


def execution():
    """Function to execute the query
    Creates a connection to the base, executes the query, closes the cursor
    and database and handles operationalError
    """
    if len(sys.argv) == 4:
        arg = sys.argv
        username, password, database = arg[1:]
        # creating a connection to a database called hbtn_0e_0_usa
        db = MySQLdb.Connect(password=password,
                             user=username, database=database)

        # cursor
        try:
            cur = db.cursor()
            cur.execute("SELECT * FROM states ORDER BY id")
            state = cur.fetchall()
        except MySQLdb.OperationalError as e:
            if e[0] == 1060:
                pass
            else:
                raise
        for row in state:
            print(str(row))
        # cleaning up
        cur.close()
        db.close()
    else:
        print("Usage: <python script> username, password, database")
        sys.exit(1)


if __name__ == "__main__":
    execution()
