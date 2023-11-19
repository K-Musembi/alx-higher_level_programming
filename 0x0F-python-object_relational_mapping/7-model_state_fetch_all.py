#!/usr/bin/python3
'''List all state objects from database'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

username = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]

engine = create_engine(
        f"mysql://{username}:{password}@localhost:3306/{db_name}")

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

states = session.query(State).order_by(State.id).all()

for state in states:
    print(f"{state.id}: {state.name}")


def main():
    '''empty function'''

    ...


if __name__ == "__main__":
    main()
