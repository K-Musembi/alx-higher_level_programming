#!/usr/bin/python3
'''Print all city objects'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv


if len(argv) == 4:
    engine = create_engine(
            f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")

    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    cities = session.query(City, State)\
            .join(State, State.id == City.state_id)\
            .order_by(City.id)\
            .all()

    for city, state in cities:
        print(f"{state.name}: {city.id} {city.name}")


def main():
    '''empty function'''

    ...


if __name__ == "__main__":
    main()
