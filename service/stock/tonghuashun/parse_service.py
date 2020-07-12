import xml.etree.ElementTree as ElementTree
from bs4 import BeautifulSoup
from utils import logger
from utils.time import time_format
import datetime
import traceback
import json
import re
import math


class TonghuashunParseService:

    @classmethod
    def format_quotations(self, content):
        stock_list = []
        soup = BeautifulSoup(content, "html.parser")
        table_list = soup.find_all('tbody')
        for table in table_list:
            tr_list = table.find_all('tr')
            for tr in tr_list:
                td_list = tr.find_all('td')
                stock = {
                    "stock_code": td_list[1].text,
                    "stock_name": td_list[2].text,
                    'curr_price': td_list[3].text,
                    'circulation_stock': td_list[11].text,
                }
                if td_list[11].text.find('万') >= 0:
                    money = td_list[11].text.split('万')
                    stock['circulation_stock'] = float(money[0]) * 10000
                elif td_list[11].text.find('亿') >= 0:
                    money = td_list[11].text.split('亿')

                    stock['circulation_stock'] = float(money[0]) * 100000000

                stock_list.append(stock)
        return stock_list


ths_parse_svc = TonghuashunParseService()
