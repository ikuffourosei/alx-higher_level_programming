#!/usr/bin/python3
"""a script that lists all State objects from the database hbtn_0e_6_usa
"""


import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    username, passwd, dbs = sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, passwd, dbs))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for row in session.query(State).order_by(State.id):
        print(f"{row.id}: {row.name}")
    session.close()
    