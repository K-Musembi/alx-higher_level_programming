#!/usr/bin/python3
'''Change name of state'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if len(argv) == 4:
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    engine = create_engine(
            f"mysql://{username}:{password}@localhost:3306/{db_name}")

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    state = session.query(State).filter_by(id=2).first()
    if state:
        state.name = "New Mexico"
        session.commit()
    else:
        pass


def main():
    '''Empty function'''

    ...


if __name__ == "__main__":
    main()
