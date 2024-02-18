#!/usr/bin/python3
import sys
import MySQLdb


def connection():
    cli = sys.argv
    if len(cli) == 5:
        username, password, database, name = cli[1:]
        db = MySQLdb.connect(port=3306, user=username, host="localhost",
                             password=password, database=database)
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
