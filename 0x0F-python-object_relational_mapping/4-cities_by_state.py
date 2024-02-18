#!/usr/bin/python3
import sys
import MySQLdb



def connection():
    cli = sys.argv
    if len(cli) == 4:
        username, password, database = cli[1:]
        db = MySQLdb.connect(port=3306, user=username, host='localhost',
                             password=password, database=database)
        try:
            cur = db.cursor()
            cur.execute("""SELECT cities.id, cities.name, states.name
                        FROM cities JOIN states
                        ON cities.state_id=states.id
                        ORDER BY cities.id""")
            allCites = cur.fetchall()
        except MySQLdb.OperationalError as e:
            if e[0] == 1060:
                pass
            else:
                raise
        for items in allCites:
            print(str(items))

        # cleaning up
        cur.close()
        db.close()
    else:
        print(f"Usage: <python script> username, password, database")
        sys.exit(1)


if __name__ == "__main__":
    connection()
