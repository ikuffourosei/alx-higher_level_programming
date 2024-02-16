#!/usr/bin/python3
import MySQLdb as msdb
import sys

def execution():
    
    if len(sys.argv) == 4:
        arg = sys.argv
        username, password, database = arg[1:]
        #creating a connection to a database called hbtn_0e_0_usa
        db = msdb.Connect(password=password, user=username, database=database)

        # cursor
        try:
            cur = db.cursor()
            cur.execute("SELECT * FROM states ORDER BY id")
            state = cur.fetchall()
        except msdb.OperationalError as e:
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
