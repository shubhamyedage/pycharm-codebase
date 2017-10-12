"""
https://docs.python.org/3.1/library/logging.html
"""

import logging
from logging import FileHandler, Formatter, handlers, StreamHandler

class LogHandler:
    def get_logger(self, name):
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        formatter = Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # Console Handler.
        console_handler = StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # File Handler
        file_handler = FileHandler(filename="ee.log")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        return logger


l = LogHandler().get_logger("test")
l.info("hey!!!!!!!!!!!!!!!!!!!!!!!!!!")