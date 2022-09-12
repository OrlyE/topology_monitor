import logging
from logging.handlers import RotatingFileHandler


class Logger(object):
    _LOG = None

    @staticmethod
    def __create_logger(log_name, log_level, handler):
        """
        A private method that interacts with the python
        logging module
        """
        # set the logging format
        log_format = "%(asctime)s:%(levelname)s:%(message)s"

        # Initialize the class variable with logger object
        Logger._LOG = logging.getLogger(log_name)
        logging.basicConfig(level=logging.INFO, format=log_format, datefmt="%Y-%m-%d %H:%M:%S")

        # set the logging level based on the user selection
        if log_level == "INFO":
            Logger._LOG.setLevel(logging.INFO)
        elif log_level == "ERROR":
            Logger._LOG.setLevel(logging.ERROR)
        elif log_level == "DEBUG":
            Logger._LOG.setLevel(logging.DEBUG)

        if handler:
            Logger._LOG.addHandler(handler)
        return Logger._LOG

    @staticmethod
    def get_logger(log_name=__name__, log_level=logging.INFO, handler_name=None):
        """
        A static method called by other modules to initialize logger in
        their own module
        """
        handler = None
        if handler_name:
            if handler_name == 'file':
                handler = get_file_handler
        logger = Logger.__create_logger(log_name, log_level, handler)

        # return the logger object
        return logger


def get_file_handler(default_path = "./loggi.log"):
    max_bytes = 100 * 1024 * 1024  # 100MB
    backup_rolling_files = 3

    return RotatingFileHandler(default_path, maxBytes=max_bytes, backupCount=backup_rolling_files)

