#!/usr/bin/python3
'''Delete states with a'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

engine = create_engine(f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")

DBSession = sessionmaker(bind=engine)
session = DBSession()

a_named = session.query(State).filter(State.name.like('%a%')).all()

for state in a_named:
    session.delete(state)

session.commit()


def main():
    '''empty function'''

    ...


if __name__ == "__main__":
    main()
