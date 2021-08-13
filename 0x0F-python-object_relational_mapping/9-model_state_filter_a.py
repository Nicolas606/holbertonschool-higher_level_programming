#!/usr/bin/python3
""" Module: 9-model_state_filter_a.py """

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

    q_sql = session.query(State).filter(State.name.like("%a%"))
    result = q_sql.all()

    for i in result:
        print("{}: {}".format(i.id, i.name))

    session.close()
