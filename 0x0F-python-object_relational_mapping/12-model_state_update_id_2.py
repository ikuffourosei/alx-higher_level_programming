#!/usr/bin/python3
"""a script that changes the name of a State object from the
database hbtn_0e_6_usa
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username, passwd, dbs = argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, passwd, dbs), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # change name of state where id = 2
    state = session.query(State).order_by(State.id).filter_by(id=2).first()
    state.name = 'New Mexico'
    session.commit()
    session.close()
