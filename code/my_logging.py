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


if __name__ == '__main__':
    test()
