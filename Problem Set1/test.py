# coding=utf-8
from base import Session, engine, Base
from sailorboat_part2 import Boat, Sailor, Reserve
from sqlalchemy import func, distinct
from sqlalchemy import text
import sqlalchemy.orm
import sqlalchemy.ext.declarative
from datetime import date

def stmt2():
    with engine.connect() as conn:
        result = conn.execute("select b.bid, b.bname, count(*) from reserves r join boats b on b.bid = r.bid where not b.bid = 0 group by bid;")
        rows = result.fetchall()
        result_bid = []
        result_bname = []
        result_count = []
        for r in rows:
            result_bid.append(r[0])
            result_bname.append(r[1])
            result_count.append(r[2])
        return result_bid, result_bname, result_count

def test_stmt2():
    expected_bid = [101, 102, 103, 104, 105, 106, 109, 112, 110, 107, 111, 108]
    expected_bname = ["Interlake", "Interlake", "Clipper", "Clipper", "Marine", "Marine", "Driftwood", "Sooney", "Klapser", "Marine", "Sooney", "Driftwood"]
    expected_count = [2, 3, 3, 5, 3, 3, 4, 1, 3, 1, 1, 1]
    result_bid, result_bname, result_count = stmt2()
    assert sorted(result_bid) == sorted(expected_bid) and sorted(result_bname) == sorted(expected_bname) and sorted(result_count) == sorted(expected_count)

def stmt6():
    with engine.connect() as conn:
        result = conn.execute("select s.sname from sailors s where s.sid not in (select r.sid from reserves r where r.bid in (select b.bid from boats b where b.color = 'red'));")
        rows = result.fetchall()
        result = []
        for r in rows:
            result.append(r[0])
        return result


def test_stmt6():
    expected = ["brutus", "andy", "rusty", "jit", "zorba", "horatio", "art", "vin", "bob"]
    result = stmt6();
    assert sorted(expected) == sorted(result)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# load in all data entries from data.txt
with open('./data.txt', 'r') as fp:
    for line in fp:
        line = line.strip('\n')
        with engine.connect() as conn:
            conn.execute(line);

test_stmt2()
test_stmt6()

session = Session()
session.commit()
session.close()
