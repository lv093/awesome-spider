from kafka import KafkaProducer
from kafka import errors as KErrors
# from kafka import KafkaConsumer
import random
import json
import time
# from config.app import Config
from config import app_config
from utils import logger


class Kafka:
    kafka_host = ''
    # kafka_port = ''
    producer = None

    def __init__(self):
        host = app_config.get("KAFKA_SOCCER_HOST")
        # port = Config.KAFKA_SOCCER_PORT
        self.set_host(host)

    def init_kafka(self):
        res = self.set_host(app_config.get("KAFKA_SOCCER_HOST"))
        if res is not None:
            logger.info("初始化kafka成功")
        else:
            logger.info("初始化kafka失败")

    def set_host(self, hosts):
        if type(hosts) == list:
            host = hosts    # random.sample(hosts, 1)
        elif type(hosts) == str:
            host = hosts.split(',')
        elif type(hosts) == tuple:
            host = list(hosts)
        else:
            return None
        self.kafka_host = host
        # self.kafka_port = port
        self.producer = None#KafkaProducer(bootstrap_servers=self.kafka_host, connections_max_idle_ms=60 * 60 * 1000, retries=1,retry_backoff_ms=50)
        if self.producer is None:
            return None
        # self.producer = KafkaProducer(bootstrap_servers=['{kafka_host}:{kafka_port}'.format(
        #     kafka_host=self.kafka_host,
        #     kafka_port=self.kafka_port
        # )])
        return True

    # 默认是异步发送
    def send_msg(self, topic, command, msg, hash_key=None):

        msgArr = {
            'command': command,
            'data': msg,
            'topic': topic,
            'timestamp': str(time.time()),
        }
        msgstr = json.dumps(msgArr)
        try:
            if self.producer is None:
                self.init_kafka()
            future = self.producer.send(topic, msgstr.encode('utf-8'), hash_key)
            result = future.get(timeout=10)
        except KErrors.KafkaTimeoutError as error:
            logger.error(error)
            result = None
        return result

    def get_msg(self, msg):
        if 'm' not in msg.keys():
            return False
        try:
            data = json.loads(msg['m'])
        except Exception as err:
            logger.info("数据格式错误[%s]msg[%s]", err, msg)
            return False
        if 'command' not in data.keys() or 'data' not in data.keys() or 'topic' not in data.keys():
            logger.info("数据格式错误[%s]", data)
            return False
        return data

    def reset(self):
        self.stop_kafka()
        self.init_kafka()

    def stop_kafka(self):
        if self.producer is None:
            return True
        self.producer.close()

    def __del__(self):
        if self.producer is None:
            return True
        self.producer.close()


KafkaClient = Kafka()

# KafkaClient = 111#Kafka('10.9.194.192', '9092')
# data = {
#     'comment_uid': 123,
#     'incr': 100,
# }
# test.sendMsg('afCommentUp', 'user@up', data)
