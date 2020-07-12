from random import choice

user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/534.51.22 (KHTML, like Gecko) Version/5.1.1 Safari/534.51.22',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
    'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)'
]

mobile_user_agent_list = [
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A5365b MicroMessenger/6.7.2 NetType/WIFI Language/zh_CN',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3',
    'Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F5027d Safari/600.1.4',
    'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_2 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5',
    'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10',
    'Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 MicroMessenger/6.7.3(0x16070321) NetType/WIFI Language/en',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 MicroMessenger/6.7.3(0x16070321) NetType/WIFI Language/en',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.8.2 Mobile/15B87 Safari/604.1 MttCustomUA/2 QBWebViewType/1 WKType/1',
    'Mozilla/5.0 (iPhone 6s; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.3.0 Mobile/15B87 Safari/604.1 MttCustomUA/2 QBWebViewType/1 WKType/1',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0 MQQBrowser/8.8.2 Mobile/14B72c Safari/602.1 MttCustomUA/2 QBWebViewType/1 WKType/1',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_2 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A421 MicroMessenger/6.3.22 Language/en',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 MicroMessenger/6.3.22 Language/en',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0 MQQBrowser/8.8.2 Mobile/14B100 Safari/602.1 MttCustomUA/2 QBWebViewType/1 WKType/1'
]

proxy_http_list = [
    'http://218.60.8.83:3129',
    'http://117.158.189.238:9999',
    'http://182.150.35.173:80',
    'http://36.110.211.102:80',
    'http://124.47.34.200:80',
    'http://222.186.58.65:1080',
    'http://182.150.35.86:8080',
    'http://183.47.40.35:8088',
    'http://113.200.214.164:9999',
]

proxy_https_list = [
    'https://175.154.202.72:4216',
    'https://36.57.76.99:4248',
    'https://117.57.34.95:4226',
    'https://112.85.178.73:4216',
    'https://122.242.63.19:4256',
    'https://36.34.12.54:6436',
    'https://60.166.95.33:2644',
    'https://182.247.61.202:4273',
    'https://58.241.203.27:4203',
    'https://123.97.105.194:4258',
    'https://114.250.170.192:4273',
    'https://113.121.156.52:5649',
    'https://49.84.38.195:4207',
    'https://110.82.195.104:4216',
    'https://117.84.119.196:4232',
]

mobile_user_whoscore = ["WSMobile/1.5.1 (iPhone; iOS 12.3.1; Scale/2.00)",
                        "WSMobile/1.5.1 (iPhone; iOS 10.2.1; Scale/2.00)",
                        "WSMobile/1.5.1 (iPhone; iOS 10.3; Scale/2.00)",
                        "WSMobile/1.5.1 (iPhone; iOS 10.3.1; Scale/2.00)",
                        "WSMobile/1.5.1 (iPhone; iOS 10.3.2; Scale/2.00)",
                        "WSMobile/1.5.1 (iPhone; iOS 10.3.3; Scale/2.00)",
                        "WSMobile/1.5.1 (iPhone; iOS 11.0.1; Scale/2.00)",
                        "WSMobile/1.5.1 (iPhone; iOS 11.0.2; Scale/2.00)",
                        "WSMobile/1.5.1 (iPhone; iOS 11.0.3; Scale/2.00)",
                        "WSMobile/1.5.1 (iPhone; iOS 11.1; Scale/2.00)",
                        "WSMobile/1.5.1 (iPhone; iOS 11.1.1; Scale/2.00)",
                        "WSMobile/1.5.1 (iPhone; iOS 11.1.2; Scale/2.00)",
                        "WSMobile/1.5.1 (iPhone; iOS 11.2; Scale/2.00)",
                        "WSMobile/1.5.1 (iPhone; iOS 11.2.1; Scale/2.00)",
                        "WSMobile/1.5.1 (iPhone; iOS 11.2.2; Scale/2.00)",
                        "WSMobile/1.5.1 (iPhone; iOS 11.2.5; Scale/2.00)",
                        "WSMobile/1.5.1 (iPhone; iOS 11.2.6; Scale/2.00)",
                        "WSMobile/1.5.1 (iPhone; iOS 11.3; Scale/2.00)",
                        "WSMobile/1.5.1 (iPhone; iOS 11.3.1; Scale/2.00)",
                        "WSMobile/1.5.1 (iPhone; iOS 11.4; Scale/2.00)",
                        "WSMobile/1.5.1 (iPhone; iOS 11.4.1; Scale/2.00)",
                        "WSMobile/1.5.1 (iPhone; iOS 12.1; Scale/2.00)",
                        "WSMobile/1.5.1 (iPhone; iOS 12.1.1; Scale/2.00)",
                        "WSMobile/1.5.1 (iPhone; iOS 12.1.4; Scale/2.00)",
                        "WSMobile/1.5.1 (iPhone; iOS 12.4.2; Scale/2.00)",
                        "WSMobile/1.5.1 (iPhone; iOS 13.2.1; Scale/2.00)",
                        "WSMobile/1.5.1 (iPhone; iOS 13.1.2; Scale/2.00)",
                        "WSMobile/1.5.1 (iPhone; iOS 13.1.3; Scale/2.00)",
                        ]


def get_random_user_agent():
    return choice(user_agent_list)


def get_random_mobile_user_agent():
    return choice(mobile_user_agent_list)

def get_random_ws_user_agent():
    return choice(mobile_user_whoscore)


def get_random_proxy():
    return {'http': choice(proxy_http_list), 'https': choice(proxy_https_list)}
