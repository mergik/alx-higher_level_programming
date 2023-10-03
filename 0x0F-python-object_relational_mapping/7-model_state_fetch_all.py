#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username, password, database = argv[1:4]
    db_uri = f'mysql+mysqldb://{username}:{password}@localhost/{database}'
    engine = create_engine(db_uri, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State):
        print(f"{state.id}: {state.name}")
    session.close()
