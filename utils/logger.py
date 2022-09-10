import logging
from datetime import datetime
from logging.handlers import RotatingFileHandler
from pythonjsonlogger import jsonlogger

DEFAULT_FORMAT = '%(asctime)s %(pathname)s:%(lineno)d %(levelname)s %(message)s'
DEFAULT_PATH = "./logi.log"
MAX_BYTES = 100 * 1024 * 1024  # 100MB
BACKUP_ROLLING_FILES = 3


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get('ts'):
            # this doesn't use record.created, so it is slightly off
            now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            log_record['ts'] = now
        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname
        if log_record.get('org'):
            log_record['org'] = log_record.get('org')
        else:
            log_record['org'] = log_record.get('org')


def get_logger(log_name=__name__, logging_lvl=logging.INFO, stream=False, fmt=DEFAULT_FORMAT, path=DEFAULT_PATH):
    logger = logging.getLogger(log_name)
    logger.setLevel(level=logging_lvl)
    file_handler = RotatingFileHandler(path, maxBytes=MAX_BYTES, backupCount=BACKUP_ROLLING_FILES)
    formatter = CustomJsonFormatter('(ts) (level) (msg) (org) (pathname)')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    if stream is True:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
    logger.info("Logger initialized successfully!")
    return logger
