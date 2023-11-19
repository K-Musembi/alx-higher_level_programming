#!/usr/bin/python3
'''List first state'''

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

first = session.query(State).order_by(State.id).first()

if first is None:
    print("Nothing")
else:
    print(f"{first.id}: {first.name}")


def main():
    '''empty function'''

    ...


if __name__ == "__main__":
    main()
