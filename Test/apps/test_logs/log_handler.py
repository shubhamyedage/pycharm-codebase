import os
import logging.config


class LogHandler(object):

    def __init__(self):
        # load logging.conf config file.
        config_log_path = "logging.conf"
        logging.config.fileConfig(config_log_path)
        # filename = "example.log"
        # logging.basicConfig(filename=filename, level=logging.INFO)

    def get_logger(self, logger_name):
        # create logger
        logger = logging.getLogger(logger_name)
        return logger
