from sqlalchemy import Column, String, Integer
from base import Base, engine

class Cost(Base):
    __tablename__ = 'costs'
    bid = Column(Integer, primary_key=True)
    pid = Column(Integer, primary_key=True)

    def __init__(self, pid, cid):
        self.bid = bid
        self.cid = cid

class Price(Base):
    __tablename__ = 'prices'
    pid = Column(Integer, primary_key=True)
    ptype = Column(String(20))
    price_num = Column(Integer)

    def __init__(self, pid, ptype, price_bum):
        self.pid = pid
        self.ptype = ptype
        self.price_num = price_num
