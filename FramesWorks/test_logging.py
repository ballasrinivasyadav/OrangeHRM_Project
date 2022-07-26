import logging

def test_loggingDemo():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s") #MAIN
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler) #filehandle object

    logger.setLevel(logging.WARNING)

    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("something is warning mode")
    logger.critical("it is in critical mode")