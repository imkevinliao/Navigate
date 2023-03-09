import logging
import sys


class Log:
    """
    how to use ? [you can see test() function]
    import this file, then Log(), you can config paras in Log().
    such as Log(filepath = "/home/ubuntu/kevin/mylog.log",output_to_file = True, level = logging.DEBUG)
    """

    def __init__(self, format="%(asctime)s %(levelname)s [line:%(lineno)d] %(message)s",
                 datefmt="%Y-%m-%d %H:%M:%S(%p)", level=logging.INFO, encoding="utf-8", filepath='default.log',
                 filemode='a+', output_to_file=False):
        self.format = format
        self.datefmt = datefmt
        self.level = level
        self.encoding = encoding
        self.filepath = filepath
        self.filemode = filemode
        self.output_to_file = output_to_file
        self.handlers = f"""[logging.FileHandler(filename={self.filepath}, encoding='{self.encoding}]', mode='{self.filemode}')]"""
        self.main()
        ...

    def main(self):
        if sys.version_info > (3, 9):
            if self.output_to_file:
                logging.basicConfig(format=self.format, datefmt=self.datefmt, level=self.level, encoding=self.encoding,
                                    filemode=self.filemode, filename=self.filepath)
            else:
                logging.basicConfig(format=self.format, datefmt=self.datefmt, level=self.level, encoding=self.encoding,
                                    filemode=self.filemode)
        else:
            if self.output_to_file:
                logging.basicConfig(format=self.format, datefmt=self.datefmt, level=self.level,
                                    handlers=[logging.FileHandler(filename=self.filepath,
                                                                  encoding=self.encoding,
                                                                  mode=self.filemode)])
            else:
                logging.basicConfig(format=self.format, datefmt=self.datefmt, level=self.level)


def test():
    Log(level=logging.DEBUG, filepath="default.log", output_to_file=False)
    logging.debug("debug:log config.")
    logging.info("info:log config")
    logging.warning("warning:log config")
    logging.error("error:log config")

class MyLog(object):
    """
    使用方式，复制class到需要用的地方
    MyLog() or MyLog(log_name = "./out.log")
    """

    def __init__(self, log_name=None):
        self.__filename = log_name
        self.my_init()
        ...

    @staticmethod
    def test():
        logging.debug("hello debug 中文")
        logging.info("hello info 中文")
        logging.warning("hello warning 中文")
        logging.error("hello error 中文")

    def my_init(self):
        logger = logging.getLogger()

        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s [line:%(lineno)d] %(message)s",
                                      datefmt="%Y-%m-%d %H:%M:%S(%p)")

        stdout_handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(stdout_handler)
        stdout_handler.setFormatter(formatter)

        if self.__filename:
            file_handler = logging.FileHandler(filename=self.__filename, encoding='utf-8')
            logger.addHandler(file_handler)
            file_handler.setFormatter(formatter)
            
if __name__ == '__main__':
    test()

# -----------------------------------------------下面是我对log最初的认识 使用 basicConfig 现在已经不使用这种方式了----------------------------------------------------------------    
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

# ------------------------------ 补充说明 -----------------------------------------
"""
在实际使用 logging 模块的过程中，遇到的问题，现在解决一下。 关于日志的输出，我们希望日志既能够输出到控制台，同时也能持久化到文件，这个时候，上面的日志配置方式就没法解决。
"""
import logging
import sys

logger = logging.getLogger()

# 我们对logger设置了日志级别，事实上可以在handler中设置 file_handler.setLevel(logging.INFO)
# 日志分级的问题，例如我们希望 info.log, debug.log, error.log, 设置多个 file_hander 即可。（一般情况下日志不必分的如此细，没有必要）
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(filename="output.log", encoding='utf-8')
stdout_handler = logging.StreamHandler(sys.stdout)

formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s [line:%(lineno)d] %(message)s",
                              datefmt="%Y-%m-%d %H:%M:%S(%p)")
file_handler.setFormatter(formatter)
stdout_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stdout_handler)

for i in range(3):
    logger.debug("This is 中文 " + str(i))
for i in range(3):
    logger.info("Here is 中文 " + str(i))

# ------------------------------- END --------------------------------------------
