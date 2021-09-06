import logging

_log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"

def get_file_handler(f = "sample.log", lvl = "INFO", formatter=_log_format):
    '''
    creates file handler.
    f           - log file (str),
    lvl         - logging level,
    formatter   - output pattern.
    '''
    file_handler = logging.FileHandler(f)
    file_handler.setLevel(lvl)
    file_handler.setFormatter(logging.Formatter(formatter))
    return file_handler

def get_stream_handler(lvl = "WARNING", formatter=_log_format):
    '''
    creates stream handler, output messages in STDOUT by default.
    lvl         - logging level,
    formatter   - output pattern.
    '''
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(lvl)
    stream_handler.setFormatter(logging.Formatter(formatter))
    return stream_handler

def get_logger(name, lvl = "INFO"):
    '''
    creates a logger.
    name        - module name for logging,
    lvl         - logging level.
    '''
    logger = logging.getLogger(name)
    logger.setLevel(lvl)
    logger.addHandler(get_file_handler())
    logger.addHandler(get_stream_handler())
    return logger

if __name__ == "__main__":
    logger = get_logger(__name__)
    logger.info("Logger initialized")
    logger.warning("end of the prog")