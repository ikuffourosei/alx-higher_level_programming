#!/usr/bin/python3
"""contains the class definition of a City
"""


from model_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """inherits from Base (imported from model_state)
    links to the MySQL table cities
    class attribute id that represents a column of an auto-generated,
    unique integer, cannot be null and is a primary key
    class attribute name that represents a column of a string of 128 characters
    and cannot be null
    class attribute state_id that represents a column of an integer
    cannot be null and is a foreign key to states.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
