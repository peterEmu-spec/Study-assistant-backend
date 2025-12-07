from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,Text,DateTime,create_engine
from sqlalchemy.orm import  sessionmaker 

engine =create_engine("sqlite:///study_assistant.db", echo=True)
Session=sessionmaker(bind=engine)
def get_db():
    session=Session()
    try:
        yield session
    finally:
        session.close()

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

class Study_Session(Base):
    __tablename__="study_session"

    id=Column(Integer(),primary_key=True)
    duration=Column(Integer(),)
    notes=Column(Text())
    mood=Column(Integer())
    created_at=Column(DateTime())

class Habit(Base):
    __tablename__="habit"

    id=Column(Integer(),primary_key=True)
    title=Column(Text(),nullable=False)
    frequency=Column(Text())
   
