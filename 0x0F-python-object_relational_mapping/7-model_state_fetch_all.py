#!/usr/bin/python3
""" Module : 7-model_state_fetch_all.py """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    mysql_uname = argv[1]
    mysql_upass = argv[2]
    mysql_db = argv[3]
    u_host = "localhost"

    # dialect+driver://username:password@host:port/database

    engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}".
                            format(mysql_uname, mysql_upass, u_host, mysql_db), pull_pre_ping=True)

    #link to our engine
    Session = sessionmaker(bind=engine)
    session = Session()

    q_sql = session.query(State).order_by(State.id)
    result = q_sql.all()

    for obj in result:
        print("{}: {}".format(obj.id, obj.name))

    session.close()


