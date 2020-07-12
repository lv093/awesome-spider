from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'



def create_app():
    # app = Flask(__name__)

    from config import init_config
    init_config(app)

    # from sentry import init_sentry
    # init_sentry(app)

    from model import init_db
    init_db(app)

    from controller import init_blueprint
    init_blueprint(app)
    #
    # if False and app.config.get('CRON_STATE') is True:
    #     from cron import init_cron
    #     init_cron(app)

    from utils import init_util
    init_util(app)

    # from utils.kafka import KafkaClient
    # KafkaClient.init_kafka()
    #
    # from redisdb import init_redis
    # init_redis(app)

    return app

if __name__ == '__main__':
    # for sig in [signal.SIGINT, signal.SIGHUP, signal.SIGTERM]:#, signal.SIGKILL]:
    # # signal.signal(signal.SIGINT, server_defer)
    # # signal.signal(signal.SIGTERM, server_defer)
    #     signal.signal(sig, server_defer)
    app = create_app()
    host = app.config.get('APP_HOST')
    port = app.config.get('APP_PORT')
    app.run(host, port)
