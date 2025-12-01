from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,Text,DateTime

Base=declarative_base()
class User(Base):
    __tablename__="user"

    id=Column(Integer(),primary_key=True)
    name=Column(Text(),nullable=False,unique=True)
    age=Column(Integer())
    email=Column(Text())

class Subject(Base):
    __tablename__="subject"

    id=Column(Integer(),primary_key=True)
    name=Column(Text(),nullable=False)
    difficulty=Column(Integer())
    description=Column(Text())

