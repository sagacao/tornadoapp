# coding: utf-8
#from datetime import datetime
#from sqlalchemy.orm import contains_eager, deferred
from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy import Column, DateTime, Integer, String, Boolean, Text, ForeignKey, BigInteger, DATE
from sqlalchemy import Column, Integer, String


DbBase = declarative_base()

class User(DbBase):
    __tablename__ = 'users_tb'

    userid = Column(Integer, primary_key=True)
    useraccount = Column(String(64), index=True)
    serverid = Column(Integer, nullable=False)
    level = Column(Integer)
    prof = Column(Integer)
    sex = Column(Integer)