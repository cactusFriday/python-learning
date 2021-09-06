import logging
import requests
'''
Logger and handler levels: 
0 - NOTSET
10 - DEBUG
20 - INFO
30 - WARNING
40 - ERROR
50 - CRITICAL
For logging on certain level you need to configure both logger and handler.
One logger can have many handlers
'''



logging.basicConfig(level='DEBUG')
logger = logging.getLogger()

# get all the loggers
# for key in logging.Logger.manager.loggerDict:
#     print(key)

# increase urllib3 logger logging level 
logging.getLogger('urllib3').setLevel('CRITICAL')

# set for root logger level equals to DEBUG or 10
logger.setLevel('DEBUG')

def main():
    logger.debug('Enter in the main() function')
    r = requests.get('https://www.google.com')
    print(r.headers)
if __name__ == '__main__':
    main()