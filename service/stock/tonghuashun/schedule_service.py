from service.stock.tonghuashun.client_service import ths_client_svc
from service.stock.tonghuashun.parse_service import ths_parse_svc
from service.stock.tonghuashun.save_service import ths_save_svc
from datetime import datetime, timedelta
from sqlalchemy import text
from utils.time import time_format
from utils import logger
from utils.threadpool import ThreadPool
from flask import current_app as app, g
import pickle
import time
import traceback
import json


class TonghuashunScService:

    @classmethod
    def schedule_stock_quotation(self):
        res = {}
        stock_types = ['hs', 'ss', 'zxb', 'cyb', 'kcb']
        for t in stock_types:
            page = 1
            res[t] = []
            while page < 1000:
                content = ths_client_svc.get_stock_quotation_data(t, page)
                stock_list = ths_parse_svc.format_quotations(content)
                if len(stock_list) == 0:
                    break
                res[t].append(stock_list)
                ths_save_svc.save_stock(stock_list)
                page = page+1
        return res


ths_sc_svc = TonghuashunScService()
