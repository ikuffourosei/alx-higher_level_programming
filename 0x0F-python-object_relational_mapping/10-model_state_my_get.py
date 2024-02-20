#!/usr/bin/python3
"""a script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username, passwd, dbs, state = argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, passwd, dbs), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).order_by(State.id)\
        .filter_by(name='{}'.format(state)).first()
    if result:
        print('{}'.format(result.id))
    else:
        print("Not found")
    session.close()
