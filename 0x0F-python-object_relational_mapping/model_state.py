#!/usr/bin/python3
'''Map using ORM'''

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys

Base = declarative_base()


class State(Base):
    '''Link to MySQL table'''

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
    
        engine = create_engine(
                f"mysql://{username}:{password}@localhost:3306/{db_name}")
        
        from model_city import City

        Base.metadata.create_all(engine)
