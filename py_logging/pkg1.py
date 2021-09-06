from app_logger import get_logger

logger = get_logger(__name__)

def msg_printer(msg):
    logger.info("before printing message")
    print(msg)
    logger.info("after printing message")

if __name__ == "__main__":
    pass