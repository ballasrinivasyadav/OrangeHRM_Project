import logging

def test_loggingDemo():

    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler("logfile.log")
    formatter = logging.Formatter("%(asctime)s,: %(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.debug("A debug statement is executed")
    logger.warning("Something is warning")
    logger.info("Something is mis info")
    logger.critical("something is critical")