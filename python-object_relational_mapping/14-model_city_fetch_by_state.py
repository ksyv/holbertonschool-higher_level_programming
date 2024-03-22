#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_city import City


def main():
    """Programm strt here"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], "", sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    all_cities = session.query(City).order_by('id').all()

    for city in all_cities:
        city_state = session.query(State).get(city.state_id)
        print("{}: ({}) {}".format(city_state.name, city.id, city.name))


if __name__ == '__main__':
    main()
