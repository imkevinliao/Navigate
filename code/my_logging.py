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
