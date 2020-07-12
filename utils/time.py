import time
import datetime
from dateutil import tz

class TimeFormat:
    # 生成当前时间的时间戳，只有一个参数即时间戳的位数，默认为10位，输入位数即生成相应位数的时间戳，比如可以生成常用的13位时间戳
    def now_to_timestamp(self, digits=10):
        time_stamp = time.time()
        digits = 10 ** (digits - 10)
        time_stamp = int(round(time_stamp * digits))
        return time_stamp

    # 将时间戳规范为10位时间戳
    def timestamp_to_timestamp10(self, time_stamp):
        time_stamp = int(time_stamp * (10 ** (10 - len(str(time_stamp)))))
        return time_stamp

    # 将当前时间转换为时间字符串，默认为2017-10-01 13:37:04格式
    def now_to_date(self, format_string="%Y-%m-%d %H:%M:%S"):
        time_stamp = int(time.time())
        time_array = time.localtime(time_stamp)
        str_date = time.strftime(format_string, time_array)
        return str_date

    # 将utc时间戳转为时间戳
    def date_utc_2_timestamp(self, date, format_string="%Y-%m-%d %H:%M:%S"):
        date = str(date)
        time_array = time.strptime(date, format_string)
        time_stamp = int(time.mktime(time_array)) + 8 * 3600
        return time_stamp

    # 将10位时间戳转换为时间字符串，默认为2017-10-01 13:37:04格式
    def timestamp_to_date(self, time_stamp, format_string="%Y-%m-%d %H:%M:%S"):
        time_array = time.localtime(time_stamp)
        str_date = time.strftime(format_string, time_array)
        return str_date

    # 将时间字符串转换为10位时间戳，时间字符串默认为2017-10-01 13:37:04格式
    def date_to_timestamp(self, date, format_string="%Y-%m-%d %H:%M:%S"):
        date = str(date)
        time_array = time.strptime(date, format_string)
        time_stamp = int(time.mktime(time_array))
        return time_stamp

    def prc_date_2_utc_date(self, date, format_string="%Y-%m-%d %H:%M:%S"):
        date = str(date)
        time_array = time.strptime(date, format_string)
        time_stamp = int(time.mktime(time_array)) - 8 * 3600
        date = self.timestamp_to_date(time_stamp)
        return date

    # 将时间字符串转换为10位时间戳，时间字符串默认为2017-10-01 13:37:04格式
    def cn_date_to_date(self, date, format_string="%Y-%m-%d"):
        date = str(date)
        format = ''
        if "日" in date:
            format = date.replace('年', '-').replace('月', '-').replace('日', '')
        elif "月" in date:
            format = date.replace('年', '-').replace('月', '')
            format_string = "%Y-%m"
        elif not "月" in date:
            format = date.replace('年', '')
            format_string = "%Y"
        time_array = time.strptime(format, format_string)
        str_date = time.strftime(format_string, time_array)
        return str_date

    # 获取当前UTC时间戳
    def get_cur_utc_timestamp(self):
        return int(datetime.datetime.utcnow().timestamp())

    # 获取当前UTC时间
    def get_cur_utc_date(self, format_string="%Y-%m-%d %H:%M:%S"):
        return datetime.datetime.utcnow().strftime(format_string)

    # 获取之前或之后多少时间的utc时间
    def get_utc_date_by_time(self,format_string="%Y-%m-%d %H:%M:%S", days=0, hours=0, seconds=0):
        ut_time = datetime.datetime.utcnow() + datetime.timedelta(days=days,hours=hours,seconds=seconds)
        return ut_time.strftime(format_string)

    def get_today(self):
        today = datetime.date.today()
        return today

    # 从iso格式改为其他格式
    def iso_to_tiemstamp(self, str, format_string="%Y-%m-%d %H:%M:%S"):
        data_arr = str.split('T')
        time_arr = data_arr[1].split('+')
        if format_string == '%Y-%m-%d %H:%M:%S':
            return data_arr[0] + ' ' + time_arr[0]
        if format_string == '%Y-%m-%d':
            return data_arr[0]
        if format_string == '%H:%M:%S':
            return time_arr[0]

    # 从iso格式改为其他格式
    def iso_to_tiemstamp_v2(self, str, format_string="%Y-%m-%d %H:%M:%S"):
        data_arr = str.split('T')
        time_arr = data_arr[1].split('Z')
        if format_string == '%Y-%m-%d %H:%M:%S':
            return data_arr[0] + ' ' + time_arr[0]
        if format_string == '%Y-%m-%d':
            return data_arr[0]
        if format_string == '%H:%M:%S':
            return time_arr[0]

    def date_utc_2_prc(self, date, format_string="%Y-%m-%d %H:%M:%S"):
        utc_timestamp = self.date_utc_2_timestamp(date, format_string)
        return self.timestamp_to_date(utc_timestamp, format_string)

    # 把当前时间'2017-10-01 13:37:04'字符串，转换为utc'2017-10-01 05:37:04'
    def time_to_utc_time(self, date):
        time_array = time.strptime(date, "%Y-%m-%d %H:%M:%S")
        time_struct = time.mktime(time_array)
        utc_st = datetime.datetime.utcfromtimestamp(time_struct)
        return utc_st

    def mictimestamp_to_date(self, timestamp, format_string="%Y-%m-%d %H:%M:%S"):
        time_stamp = float(timestamp/1000)
        time_arr = time.localtime(time_stamp)
        date = time.strftime(format_string,time_arr)
        return date

    '''
    %a 星期的简写。如 星期三为Web
    %A 星期的全写。如 星期三为Wednesday
    %b 月份的简写。如4月份为Apr
    %B 月份的全写。如4月份为April
    %c:  日期时间的字符串表示。（如： 04/07/10 10:43:39）
    %d:  日在这个月中的天数（是这个月的第几天）
    %f:  微秒（范围[0,999999]）
    %H:  小时（24小时制，[0, 23]）
    %I:  小时（12小时制，[0, 11]）
    %j:  日在年中的天数 [001,366]（是当年的第几天）
    %m:  月份（[01,12]）
    %M:  分钟（[00,59]）
    %p:  AM或者PM
    %S:  秒（范围为[00,61]，为什么不是[00, 59]，参考python手册~_~）
    %U:  周在当年的周数当年的第几周），星期天作为周的第一天
    %w:  今天在这周的天数，范围为[0, 6]，6表示星期天
    %W:  周在当年的周数（是当年的第几周），星期一作为周的第一天
    %x:  日期字符串（如：04/07/10）
    %X:  时间字符串（如：10:43:39）
    %y:  2个数字表示的年份
    %Y:  4个数字表示的年份
    %z:  与utc时间的间隔 （如果是本地时间，返回空字符串）
    %Z:  时区名称（如果是本地时间，返回空字符串）
    '''

    def trans_time_format(self, input, input_format, output_format="%Y-%m-%d %H:%M:%S", input_tz=None, output_tz=None):
        dt = datetime.datetime.strptime(input, input_format)

        if input_tz and output_tz:
            input_tz = tz.gettz(input_tz)
            output_tz = tz.gettz(output_tz)
            dt = dt.replace(tzinfo=input_tz)
            dt = dt.astimezone(output_tz)

        output = dt.strftime(output_format)
        return output

    def trans_bj_to_utc(self, input, input_format="%Y-%m-%d %H:%M:%S", output_format="%Y-%m-%d %H:%M:%S"):
        return self.trans_time_zone(input, input_tz='Asia/Shanghai', output_tz='UTC', input_format=input_format,
                                    output_format=output_format)

    def trans_utc_to_bj(self, input, input_format="%Y-%m-%d %H:%M:%S", output_format="%Y-%m-%d %H:%M:%S"):
        return self.trans_time_zone(input, input_tz='UTC', output_tz='Asia/Shanghai', input_format=input_format,
                                    output_format=output_format)

    def trans_time_zone(self, time_str, input_tz='Asia/Shanghai', output_tz='UTC', input_format='%Y-%m-%d %H:%M:%S',
                        output_format='%Y-%m-%d %H:%M:%S'):
        input_tz = tz.gettz(input_tz)
        output_tz = tz.gettz(output_tz)
        dt = datetime.datetime.strptime(time_str, input_format)
        dt = dt.replace(tzinfo=input_tz)
        output = dt.astimezone(output_tz).strftime(output_format)
        return output

    def trans_date_to_time_str(self, info, format="%Y-%m-%d %H:%M:%S"):
        if not info:
            return ''
        return datetime.datetime.strftime(info, format)

    # 从当前时间往前往后 跳num天
    def skip_day(self, num):
        today = datetime.date.today()
        oneday = datetime.timedelta(days=num)

        skip_day = today - oneday
        return skip_day

    def date_delta(self, date, format_string="%Y-%m-%d %H:%M:%S", days=1, hours=0, minutes=0, seconds=0):
        inner_format_string = "%Y-%m-%d %H:%M:%S"
        if len(date) < 11:
            inner_format_string = format_string.split(' ')[0]
        d1 = datetime.datetime.strptime(date, inner_format_string)
        delta = datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
        n_days = d1 + delta
        return str(n_days.strftime(format_string))

    # date:datetime 格式 CET:伦敦时区
    def trans_zone_date(self, date=datetime.datetime.now(), tz_str='UTC', format_string="%Y-%m-%d %H:%M:%S"):
        to_zone = tz.gettz(tz_str)
        return date.astimezone(to_zone).strftime(format_string)

    # 将北京时间转换为utc时间戳
    @classmethod
    def date_bj_2_utc_timestamp(cls, date, format_string="%Y-%m-%d %H:%M:%S"):
        date = str(date)
        time_array = time.strptime(date, format_string)
        time_stamp = int(time.mktime(time_array)) - 8 * 3600
        return time_stamp

    def get_utc_time(self, date, format="%Y/%m/%d %H:%M:%S"):
        if date == '' or date is None:
            return None
        time_array = datetime.datetime.strptime(date, format)
        utc_st = time_array.strftime('%Y-%m-%d %H:%M:%S')
        return utc_st


time_format = TimeFormat()
