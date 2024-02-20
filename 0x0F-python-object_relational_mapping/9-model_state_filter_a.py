#!/usr/bin/python3
"""a script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username, passwd, dbs = argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, passwd, dbs))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    a = session.query(State).order_by(State.id.asc()).filter(State.name.like('%a%'))
    for rows in a:
        print(f"{rows.id}:{rows.name}")
    session.close()
