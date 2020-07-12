from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP, Text, Date, Float, MetaData, event, BigInteger
from model import db
from model.base_model import BaseModel


class Stock(BaseModel, db.Model):
    __tablename__ = 'stocks'
    __bind_key__ = 'stock_data'
    __unique_attr__ = ['stock_code']

    id = Column(Integer, primary_key=True)
    stock_code = Column(String, nullable=False)
    stock_name = Column(String)
    curr_price = Column(Float)
    circulation_stock = Column(Integer)
