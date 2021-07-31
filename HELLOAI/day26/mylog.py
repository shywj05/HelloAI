import logging


class Mylog:

    def getLogger(self):
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        logger = logging.getLogger('Mylog')
        logger.setLevel(logging.DEBUG)
        
        if len(logger.handlers) > 0:
            return logger  # Logger already exists

        ch = logging.StreamHandler()
        fh = logging.FileHandler(filename="Mylog.log")

        logger.addHandler(ch)
        logger.addHandler(fh)
        
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        return logger
