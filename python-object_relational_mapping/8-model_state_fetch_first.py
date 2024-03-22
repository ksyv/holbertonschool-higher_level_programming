#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def main():
    """Programm strt here"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], "", sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).first()

    if first_state:
        print(str(first_state.id) + ": " + first_state.name)
    else:
        print("Nothing")


if __name__ == '__main__':
    main()
