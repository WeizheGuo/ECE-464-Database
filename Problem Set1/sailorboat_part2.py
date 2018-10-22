from sqlalchemy import Column, String, Integer, Date
from base import Base, engine


class Reserve(Base):
    __tablename__ = 'reserves'
    sid = Column(Integer, primary_key=True)
    bid = Column(Integer, primary_key=True)
    day = Column(Date, primary_key=True)

    def __init__(self, sid, bid, day):
        self.sid = sid
        self.bid = bid
        self.day = day


class Sailor(Base):

    __tablename__ = 'sailors'
    sid = Column(Integer, primary_key=True)
    sname = Column(String(30))
    rating = Column(Integer)
    age = Column(Integer)

    def __init__(self, sid, sname, rating, age):
        self.sid = sid
        self.sname = sname
        self.rating = rating
        self.age = age


class Boat(Base):
    __tablename__ = 'boats'
    bid = Column(Integer, primary_key=True)
    bname = Column(String(20))
    color = Column(String(10))
    length = Column(Integer)

    def __init__(self, bid, bname, color, length):
        self.bid = bid
        self.bname = bname
        self.color = color
        self.length = length

