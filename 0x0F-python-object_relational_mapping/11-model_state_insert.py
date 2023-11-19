#!/usr/bin/python3
'''Add a new state'''

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

new_state = State(name="Louisiana")

session.add(new_state)
session.commit()

print(new_state.id)


def main():
    '''Empty function'''
    ...


if __name__ == "__main__":
    main()
