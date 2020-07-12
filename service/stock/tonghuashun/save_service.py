from model.stock.stock import *
from utils.string import util_string
from utils.time import time_format
from utils import logger
from flask import current_app as app
import math
import json

"""
  球探数据存储服务
"""


class TonghuashunSaveService:

    @staticmethod
    def save_stock(data):
        stock_orm = Stock()
        stock_orm.sync_batch(data)
        return []

ths_save_svc = TonghuashunSaveService()
