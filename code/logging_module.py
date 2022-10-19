import logging

# https://www.cnblogs.com/yyds/p/6901864.html
# https://realpython.com/python-logging/

# LOG_FORMAT = "%(asctime)s %(levelname)s: %(message)s"
# LOG_DATE_FORMATE = "%Y-%m-%d %H:%M:%S(%p)"
# LOG_FILENAME = "app.log"

# logging.basicConfig(format=LOG_FORMAT, datefmt=LOG_DATE_FORMATE, level=logging.INFO, filename=LOG_FILENAME)

# python 3.9 basicConfig 才有参数：encoding="utf-8"，解决log中文乱码问题. 这里使用handlers解决
logging.basicConfig(format="%(asctime)s %(levelname)s [line:%(lineno)d] %(message)s", datefmt="%Y-%m-%d %H:%M:%S(%p)",
                    level=logging.INFO,
                    handlers=[logging.FileHandler(filename="app.log", encoding='utf-8', mode='a+')])


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

logging.fatal("致命错误")

# 日志级别
# DEBUG（10）、INFO（20）、WARNING（30）、ERROR（40）、CRITICAL（50）
