import requests

"""
RPC工具
"""


class Rpc:

    # 发送请求
    def get_request(self, url, param={}, headers={}):
        res = []
        try:
            req = requests.Session()
            req.params = param
            req.headers = headers
            res = req.get(url)
        except Exception as err:
            print(err)
            pass  # TODO 处理异常，

        # TODO 判断结果状态码
        if res.status_code != 200:
            return '接口返回状态异常'  # todo 考虑发邮件
        else:
            # TODO 判断文案
            if res.content == "":
                return '接口返回内容异常'  # todo 考虑发邮件
        return res.text

    def post_request(self, url, param={}, headers={}):
        res = []
        try:
            req = requests.Session()
            #req.params = param
            req.headers = headers
            req.verify = False
            res = req.post(url,json=param)
        except Exception as err:
            return ''

        if res.status_code != 200:
            return ''  # todo 考虑发邮件
        return res.text


util_rpc = Rpc()
