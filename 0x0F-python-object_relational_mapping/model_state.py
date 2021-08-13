#!/usr/bin/python3
""" Module: model_state.py """

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative.api import declarative_base


u_name = 'root'
u_pass = 'Root33'
port = 3306
db = 'hbtn_0e_6_usa'
u_host = 'localhost'

# dialect+driver://username:password@host:port/database
engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}".
                       format(u_name, u_pass, u_host, port, db))

Base = declarative_base()


class State(Base):
    """ class state """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
