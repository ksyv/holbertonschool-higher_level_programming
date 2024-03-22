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
    state_name = sys.argv[4]
    escape_strings = ["\x00", "\n", "\r", "\\", "'", '\"', r"\xla"]
    for i in escape_strings:
        if i in state_name:
            exit()
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states_found = session.query(State).filter(State.name == sys.argv[4]).all()

    print(states_found[0].id) if len(states_found) else print("Not found")

if __name__ == '__main__':
    main()
