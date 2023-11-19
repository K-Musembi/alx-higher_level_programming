#!/usr/bin/python3
'''List states with a'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

username = argv[1]
password = argv[2]
db_name = argv[3]

engine = create_engine(
        f"mysql://{username}:{password}@localhost:3306/{db_name}")

DBSession = sessionmaker(bind=engine)
session = DBSession()

a_named = session.query(State)\
        .filter(State.name.like('%a%'))\
        .order_by(State.id)\
        .all()

for state in a_named:
    print(f"{state.id}: {state.name}")


def main():
    '''Empty function'''

    ...


if __name__ == "__main__":
    main()
