import logging
from logging.handlers import RotatingFileHandler

def get_logger(log_file):

    logger = logging.getLogger("mintaka")

    logger.setLevel(logging.INFO)

    if not logger.handlers:

        handler = RotatingFileHandler(
            log_file,
            maxBytes=10_000_000,
            backupCount=10
        )

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(module)s:%(lineno)d | %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger