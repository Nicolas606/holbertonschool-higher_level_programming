#!/usr/bin/python3
""" Module: 8-model_state_fetch_first.py """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
if __name__ == '__main__':

    uname = argv[1]
    upass = argv[2]
    db = argv[3]

    # dialect+driver://username:password@host:port/database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(uname, upass, db), pool_pre_ping=True)

    """ link to our engine """
    Session = sessionmaker(bind=engine)
    session = Session()

    q_sql = session.query(State).order_by(State.id)
    result = q_sql.first()

    if result:
        print("{}: {}".format(result.id, result.name))
    else:
        print("Nothing")

    session.close()
