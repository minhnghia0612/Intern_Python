from sqlalchemy import Column, String,Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    username = Column(String, unique = True, index = True)
    password = Column(String)


