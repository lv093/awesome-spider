from service.stock.tonghuashun.schedule_service import ths_sc_svc
from flask import Blueprint, request, current_app,g
import json
import time

ths = Blueprint('ths', __name__)

# 股票实时行情
@ths.route('/stock_quotation', methods=['GET'])
def stock_change_check():
    data = ths_sc_svc.schedule_stock_quotation()
    return json.dumps(data)