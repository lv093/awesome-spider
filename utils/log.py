import os
import logging
import logging.handlers
import sys
from logging import raiseExceptions
from logging import Logger
from flask_log_request_id import RequestID, RequestIDLogFilter


class AppLogger(Logger):
    """
    自定义logger
    如果handler名称为console表示在终端打印所有大于等于设置级别的日志
    其他handler则只记录等于设置级别的日志
    """

    def __init__(self, name, level=logging.NOTSET):
        super(AppLogger, self).__init__(name, level)

    def callHandlers(self, record):
        """
        Pass a record to all relevant handlers.

        Loop through all handlers for this logger and its parents in the
        logger hierarchy. If no handler was found, output a one-off error
        message to sys.stderr. Stop searching up the hierarchy whenever a
        logger with the "propagate" attribute set to zero is found - that
        will be the last logger whose handlers are called.
        """
        c = self
        found = 0
        while c:
            for hdlr in c.handlers:
                found = found + 1
                if hdlr.name == 'console':
                    if record.levelno >= hdlr.level:
                        hdlr.handle(record)
                else:
                    if record.levelno == hdlr.level:
                        hdlr.handle(record)
            if not c.propagate:
                c = None  # break out
            else:
                c = c.parent
        if (found == 0) and raiseExceptions and not self.manager.emittedNoHandlerWarning:  # noqa
            sys.stderr.write("No handlers could be found for logger"
                             " \"%s\"\n" % self.name)
            self.manager.emittedNoHandlerWarning = 1


def get_logger(app, logfile_name="app", log_path="/tmp/sport-data-spider/", level=logging.DEBUG):
    '''save log to diffrent file by deffirent log level into the log path
    and print all log in console'''
    RequestID(app)
    logging.setLoggerClass(AppLogger)
    formatter = logging.Formatter(
        '%(asctime)s, %(levelname)s, %(filename)s:%(lineno)d, request_id=%(request_id)s, %(message)s', '%Y-%m-%d %H:%M:%S')

    log_files = {
        logging.DEBUG: os.path.join(log_path, logfile_name + '-debug.log'),
        logging.INFO: os.path.join(log_path, logfile_name + '-info.log'),
        logging.WARNING: os.path.join(log_path, logfile_name + '-warning.log'),
        logging.ERROR: os.path.join(log_path, logfile_name + '-error.log'),
        logging.CRITICAL:
            os.path.join(log_path, logfile_name + '-critical.log')
    }
    # 和flask默认使用同一个logger
    logger = logging.getLogger('')
    logger.setLevel(logging.DEBUG)
    for log_level, log_file in log_files.items():
        if log_level < level:
            continue
        file_handler = logging.handlers.TimedRotatingFileHandler(log_file, 'midnight')
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        file_handler.addFilter(RequestIDLogFilter())
        logger.addHandler(file_handler)

    return logger


