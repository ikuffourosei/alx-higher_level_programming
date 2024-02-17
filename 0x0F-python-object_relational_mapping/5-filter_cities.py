#!/usr/bin/python3
import sys
import MySQLdb

cli = sys.argv


def connection():
    if len(cli) == 5:
        username, password, databse, name = cli[1:]
        db = MySQLdb.connect(user=username, password=password,
                             database=databse)
        try:
            cur = db.cursor()
            cur.execute("""SELECT cities.name
                        FROM cities JOIN states
                        ON cities.state_id=states.id
                        WHERE states.name=%(name)s
                        ORDER BY cities.id""", {'name': name})
            allCites = cur.fetchall()
        except MySQLdb.OperationalError as e:
            if e[0] == 1060:
                pass
            else:
                raise
        if allCites:
            result = []
            for items in allCites:
                result.append(items[0])
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
