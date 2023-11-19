#!/usr/bin/python3
'''Map using ORM'''

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    '''Link to MySQL table'''

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    engine = create_engine(
            "mysql://root:""@localhost:3306/hbtn_0e_6_usa")

    Base.metadata.create_all(engine)
