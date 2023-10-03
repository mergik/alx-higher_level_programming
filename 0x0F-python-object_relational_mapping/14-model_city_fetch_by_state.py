#!/usr/bin/python3
"""
script that prints all City objects from the database hbtn_0e_14_usa
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username, password, database = argv[1:4]
    db_uri = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database
    )
    engine = create_engine(db_uri, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State, City).join(City).all()
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
