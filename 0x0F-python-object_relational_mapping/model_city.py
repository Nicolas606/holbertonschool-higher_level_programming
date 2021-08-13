#!/usr/bin/python3
"""Module: model_city"""

from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base, State


class City(Base):
    """Class City """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
