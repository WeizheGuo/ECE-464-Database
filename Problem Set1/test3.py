from base import Session, engine, Base
from sailorboat_part2 import Boat, Sailor, Reserve
from sailorboat_part3 import Cost, Price
from sqlalchemy import func, distinct
from sqlalchemy import text
import sqlalchemy.orm
import sqlalchemy.ext.declarative
from datetime import date

def stmt1():
    with engine.connect() as conn:
    	result = conn.execute("select price_num from prices where pid = 1;")
    	row = result.first()
    	return row[0]



def test_stmt1():
   assert stmt1() == 100

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# load in all data entries from data.txt
with open('./data.txt', 'r') as fp:
    for line in fp:
        line = line.strip('\n')
        with engine.connect() as conn:
            conn.execute(line);

test_stmt1()