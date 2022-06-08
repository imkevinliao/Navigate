import logging

# https://www.cnblogs.com/yyds/p/6901864.html
# https://realpython.com/python-logging/

# LOG_FORMAT = "%(asctime)s %(levelname)s: %(message)s"
# LOG_DATE_FORMATE = "%Y-%m-%d %H:%M:%S(%p)"
# LOG_FILENAME = "app.log"
# logging.basicConfig(format=LOG_FORMAT, datefmt=LOG_DATE_FORMATE, level=logging.INFO, filename=LOG_FILENAME)

logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S(%p)",
                    level=logging.INFO, filename="app.log")

logging.warning('Admin logged out')
logging.info('hello')
logging.debug('this is a debug info')
a = 5
b = 0

try:
    c = a / b
except ZeroDivisionError:
    logging.error("Exception occurred", exc_info=True)

name = 'John'

logging.error('%s raised an error', name)
logging.error(f'{name} raised an error')
