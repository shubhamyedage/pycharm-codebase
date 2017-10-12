from apps.test_logs.log_handler import LogHandler

logger = LogHandler().get_logger("testLogger")

logger.info("Hello World!")
logger.error("Its error!")