#!/usr/bin/python3
""" Module: model_state.py """

from sqlalchemy import create_engine  # CONNECTS US WITH THE DATABASE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.log import rootlogger
from sqlalchemy.ext.declarative import declarative_base

u_name = "root"
u_pass = "Nicolas3"
port = 3306
db = 'hbtn_0e_6_usa'
u_host = "localhost"

# CONNECTS US WITH THE DATABASE
# dialect+driver://username:password@host:port/database
engine = create_engine("mysql+msqldb://{}:{}@{}:{}/{}".
                        format(u_name, u_pass, u_host, port, db), pull_pre_ping=True)

Base = declarative_base()

class State(Base):
    """ class state """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name= Column(String(128), nullable=False)
