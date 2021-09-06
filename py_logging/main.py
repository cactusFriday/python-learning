from app_logger import get_logger
from pkg1 import msg_printer

logger = get_logger(__name__)

def main():
    logger.warning("Beginning")
    logger.info("Transmitting message")
    msg_printer("Hello from the main.py")

if __name__ == "__main__":
    main()