#!/usr/bin/python3
""" Module: 14-model_city_fetch_by_state.py """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City

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

    q_sql = session.query(State.name, City.id, City.name).join(State)
    result = q_sql.order_by(City.id).all()

    for i in result:
        print("{}: ({}) {}".formay(i[0], i[1], i[2]))
