import logging
import inspect
class UserDefinedLogger:

    def custom_logging(logLevel=logging.DEBUG):
        loggerName=inspect.stack()[1][3]
        logger=logging.getLogger(loggerName)
        logger.setLevel(logLevel)
        fh=logging.FileHandler("testyatra.log")
        formatter=logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s",datefmt="%d/%m/%Y %I:%M:%S %p")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger

    # logger.setLevel(logging.DEBUG)
    # logger.debug("this is debug message")
    # logger.info("this is info message")
    # logger.warning("this is warning message")
    # logger.error("this is error message")
    # logger.critical("this is critical message")


