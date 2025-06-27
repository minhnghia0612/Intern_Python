from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)

class Team(Base):
    __tablename__ = 'team'
    name = Column(String, primary_key=True)
    logo = Column(String)

    players = relationship("Player", back_populates="team")
    ranks = relationship("Rank", back_populates="team")
    matches = relationship("Match", back_populates="team")

class Rank(Base):
    __tablename__ = 'rank'
    id = Column(Integer, primary_key=True, autoincrement=True)
    rank = Column(Integer)
    team_name = Column(String, ForeignKey('team.name'))
    matched_played = Column(Integer)
    win = Column(Integer)
    draw = Column(Integer)
    lose = Column(Integer)
    gd = Column(Integer)
    points = Column(Integer)

    team = relationship("Team", back_populates="ranks") #1-N

class Player(Base):
    __tablename__ = 'player'
    id = Column(Integer, primary_key=True, autoincrement=True)
    player_name = Column(String)
    player_url = Column(String)
    nation = Column(String)
    pos = Column(String)
    age = Column(Integer)
    mp = Column(Integer)
    starts = Column(Integer)
    minutes = Column(Integer)

    team_name = Column(String, ForeignKey('team.name'))
    team = relationship("Team", back_populates="players")

class Match(Base):
    __tablename__ = 'match'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date)
    venue = Column(String)
    result = Column(String)
    gf = Column(Integer)
    ga = Column(Integer)
    opponent = Column(String)

    team_name = Column(String, ForeignKey('team.name'))
    team = relationship("Team", back_populates="matches")