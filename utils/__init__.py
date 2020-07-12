from .log import get_logger
import logging

logger = logging.getLogger('')


def init_util(app):
    global logger
    logger = get_logger(app, app.config['LOG_FILENAME'], app.config['LOG_PATH'], app.config['LOG_LEVEL'])
