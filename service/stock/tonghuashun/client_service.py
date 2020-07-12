from config.app import Config
from config.user_agent import user_agent_list
from utils import logger
from utils.time import time_format
import requests
import time
import datetime
import random
import json
import traceback
import execjs
from requests.adapters import HTTPAdapter


class TonghuashunClientService:

    """
    抓取js代码请求服务
    """

    # 获取必发数据
    def get_match_betfair_js(self, proxies):
        url = 'http://zhishu.35.zqsos.com:896/xml/bifa.js?' + str(time_format.get_cur_utc_timestamp()) + '000'
        header = {
            'User-Agent': random.choice(user_agent_list),
            'Referer': 'http://vip.win0168.com/betfa/index.aspx',
            'Connection': 'close',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept': '*/*'
        }
        js_code = self.do_get_request_by_proxy(url, {}, proxies, header)
        if js_code is None:
            return []
        js_code = js_code.replace('showOdds();', '')
        data = self.exec_js_code(js_code, 'B')
        return data

    # 执行js代码
    def exec_js_code(self, js_code, ret_field):
        js_code = 'function exec_js_code(){' + js_code + ' return ' + ret_field + ';}'
        ctx = execjs.compile(js_code)
        B = ctx.call('exec_js_code')
        res = []
        for b in B:
            if b is None or len(b) == 0:
                continue
            res.append(b)
        return res

    """
    抓取xml内容请求服务
    """
    def get_stock_quotation_data(self, stock_type, page):
        domain = 'http://q.10jqka.com.cn'
        prefix = '/index/index/board/'
        midfix = '/field/zdf/order/desc/page/'
        suffix = '/ajax/1/'
        url = domain + prefix + str(stock_type) + midfix + str(page) + suffix
        print(url)

        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
            'Connection': 'close',
            'Referer': 'http://vip.win0168.com/betfa/index.aspx',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept': '*/*'
        }
        xml = self.do_get_request(url=url, headers=header)
        return xml

    # 发送请求
    def do_get_request(self, url, param={}, headers={}):
        res = []
        try:
            '''
            req = requests.Session()
            req.params = param
            req.headers = headers
            req.proxies = proxies
            res = req.get(url)
            '''
            res = requests.get(url, param, headers=headers, timeout=(3, 3))
            # print(res.text)
        except Exception as err:
            return None

        # TODO 判断结果状态码
        if res is None or res.status_code != 200:
            return None  # todo 考虑发邮件
        else:
            # TODO 判断文案
            if res.text == "":
                return None  # todo 考虑发邮件
            elif res.text == "访问频率超出限制，请调慢一些。":
                return None  # todo 考虑发邮件
        return res.text.strip("\xef\xbb\xbf")

    # 获取代理
    @staticmethod
    def get_cooperation_proxy():
        return Config.PROXY_HOST_PORT  # TODO 读取环境变量

    # 发送请求
    @staticmethod
    def do_get_request_by_proxy(url, param=None, proxies=None, headers=None, time_out=3):
        if len(proxies) > 0:
            proxy = random.choice(proxies)
            protocol = proxy.split(':')[0]
            proxies = {protocol: proxy}
        else:
            proxies = {'http': 'http://106.75.79.132:31280'}
        try:
            req = requests.Session()
            req.params = param
            req.headers = headers
            req.mount('http://', HTTPAdapter(max_retries=3))
            req.mount('https://', HTTPAdapter(max_retries=3))
            req.proxies = proxies
            req.keep_alive = False
            res = req.get(url, timeout=(time_out, 3))
        except Exception as err:
            logger.error("==== 接口异常 %s %s %s %s %s", url, param, proxies, err, traceback.print_exc())
            return None
        text = res.text
        if res.status_code != 200:
            logger.error("==== 接口返回状态异常 %s %s %s %s", url, param, proxies, headers)
            return None
        else:
            if text == "" or text.find('Unauthorized') != -1 or text.find('無效用戶') != -1 or text == "操作太频繁了，请先歇一歇。":
                logger.error("==== 接口返回内容异常 %s %s %s %s %s", url, param, proxies, headers, text)
                return None

        return text


ths_client_svc = TonghuashunClientService()
