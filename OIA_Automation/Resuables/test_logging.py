import inspect
import logging


def get_logger():
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    fileHandler = logging.FileHandler('../Execution_log/OIA_Admin_test_execution_report_log.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)  # filehandler object
    logger.setLevel(logging.DEBUG)
    return logger
