#!/usr/bin/python3
"""a python file that contains the class definition of a State
and an instance Base = declarative_base():
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


Base = declarative_base()


class State(Base):
    """
    State class:
    inherits from Base
    links to the MySQL table states
    class attribute id that represents a column of an auto-generated,
    unique integer, cant be null and is a primary key
    class attribute name that represents a column of a string
    with maximum 128 characters and cant be null
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=True)
    name = Column(String(128), nullable=False)
