import logging
import inspect

def CustomLogger(loglevel=logging.DEBUG):

    # It will return the name of the method which call this method
    loggerName = inspect.stack()[1][3]
    # create a logger and set level

    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)

    # creating a handler and set level here we are creating a file handler because we want to log in a file
    handler = logging.FileHandler("automation.log", mode='w')
    handler.setLevel(loglevel)


    formatter = logging.Formatter('%(asctime)s -%(name)s - %(levelname)s: %(message)s',
                    datefmt='%d:%m:%Y %I:%M:%S %p')

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger

