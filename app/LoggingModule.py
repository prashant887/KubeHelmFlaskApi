import logging
import datetime


class GenericLogging:
    """This class is used for generic logging"""

    def __init__(self, logfile=None):
        # timestamp = datetime.date.today().strftime('%Y%m%d%H%M%S')
        if logfile is None:
            self.logfile = "{}/webapi_{}.log".format('/log', datetime.date.today().strftime('%Y%m%d'))
        else:
            self.logfile = logfile

        logger = logging.getLogger('logging')  # 'root'
        logger.propagate = False
        logger.setLevel('DEBUG')
        handler = logging.FileHandler(self.logfile)
        logger.addHandler(handler)
        formatter = logging.Formatter('%(asctime)s  | %(levelname)s | %(message)s')
        handler.setFormatter(formatter)

        self.logger = logger

    def logMsg(self, message):
        """This method is used to log info message
           Input : logger object , log message
           Output : None
        """
        self.logger.info(message)

    def logError(self, message):
        """This method is used to log error message
                   Input : logger object , log message
                   Output : None
                """
        self.logger.error(message)
