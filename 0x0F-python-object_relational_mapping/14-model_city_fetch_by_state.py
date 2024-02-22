#!/usr/bin/python3
"""a script 14-model_city_fetch_by_state.py that prints all City objects
from the database hbtn_0e_14_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    username, passwd, dbs = argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, passwd, dbs), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for s, c in session.query(State, City).filter(State.id == City.state_id)\
            .order_by(City.id).all():
        print(f"{s.name}: ({c.id}) {c.name}")
    session.close()
