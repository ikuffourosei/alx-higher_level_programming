#!/usr/bin/python3
"""a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""


import sys
import MySQLdb


def connection():
    """Function that lists all cities of a state according to user input
    """
    cli = sys.argv
    if len(cli) == 5:
        username, password, database, name = cli[1:]
        db = MySQLdb.connect(port=3306, user=username, host="localhost",
                             password=password, database=database)

        cur = db.cursor()
        cur.execute("""SELECT cities.name
                    FROM cities JOIN states
                    ON cities.state_id=states.id
                    WHERE states.name=%(name)s
                    ORDER BY cities.id ASC""", {'name': name})
        allCites = cur.fetchall()
        if allCites:
            # get the result as a list
            result = []
            for items in allCites:
                result.append(items[0])
            # show results separated with comma
            print(", ".join(result))
        else:
            print("\n")
        # cleaning up
        cur.close()
        db.close()
    else:
        print(f"Usage: <python script> username, password, database")
        sys.exit(1)


if __name__ == "__main__":
    connection()
