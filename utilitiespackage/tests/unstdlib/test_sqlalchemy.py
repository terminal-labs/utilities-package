import os

import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Sequence
from sqlalchemy import String, Integer, Float, Boolean, Column
from sqlalchemy.orm import sessionmaker

from utilitiespackage.unstdlib.sqlalchemy import enumerate_query_by_limit

filename = "/tmp/test.sqlite"
if os.path.exists(filename):
    os.remove(filename)

engine = db.create_engine("sqlite:////tmp/test.sqlite")

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
Base.metadata.create_all(engine)


class MyTable(Base):
    __tablename__ = "MyTable"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    some_col = Column(String(500))

    def __init__(self, some_col):
        self.some_col = some_col


Base.metadata.create_all(engine)


def test_sqlalchemy_enumerate_query_by_limit():
    me = MyTable("admin@example.com")
    session.add(me)
    session.commit()
    query = session.query(MyTable)
    for ele in enumerate_query_by_limit(query):
        assert ele.some_col == "admin@example.com"
