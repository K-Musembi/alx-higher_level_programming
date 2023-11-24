#!/usr/bin/python3
'''List state if found'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if len(argv) == 4:
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    search_name = argv[4]

    engine = create_engine(
            f"mysql://{username}:{password}@localhost:3306/{db_name}")

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    state_name = session.query(State)\
            .filter(State.name == search_name).first()

    if state_name:
        print(state_name.id)
    else:
        print("Not found")


def main():
    '''empty function'''

    ...


if __name__ == "__main__":
    main()
