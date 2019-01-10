from sqlalchemy import create_engine, Column, Integer, String, DateTime,Date,Boolean,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import hkstock.settings as settings


DeclarativeBase = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine('sqlite:///{}'.format(setttings.DATABASE['db']))


def create_deals_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class Stock(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "hkstock"
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column('name', String(64),nullable=True)
    symbol = Column('symbol', String(16))
    engname = Column('engname', String(128), nullable=True)
    tradetype = Column('tradetype', String(24),nullable=True)
    lasttrade = Column('lasttrade', Float,nullable=True)
    prevclose = Column('prevclose', Float,nullable=True)
    open = Column('open', Float,nullable=True)
    high = Column('high',Float,nullable=True)
    low = Column('low', Float,nullable=True)
    volume = Column('volume', Float,nullable=True)
    currentvolume = Column('currentvolume', Float,nullable=True)
    amount = Column('amount', Float,nullable=True)
    ticktime = Column('ticktime', DateTime, nullable=True)
    buy = Column('buy', Float,nullable=True)
    sell = Column('sell', Float,nullable=True)
    high_52week = Column('high_52week', Float,nullable=True)
    low_52week = Column('low_52week', Float,nullable=True)
    eps = Column('eps', Float,nullable=True)
    dividend = Column('dividend', Float,nullable=True)
    stocks_sum = Column('stocks_sum', Float,nullable=True)
    pricechange = Column('pricechange', Float,nullable=True)
    changepercent = Column('changepercent', Float,nullable=True)