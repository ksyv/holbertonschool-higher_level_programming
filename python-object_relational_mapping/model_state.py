#!/usr/bin/python3
"""Module model_state
Defines a State class that will be written to a database"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

engine = create_engine('mysql+mysqldb://root:root@localhost/hbtn_0e_6_usa')
Base = declarative_base()


class State(Base):
    """Class State
    Inherits from class Base to define what the table State
    looks like in a database.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
