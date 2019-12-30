import logging
import os
import logging.handlers
from tool.read_config import ReadConfig


class Log:

    def __init__(self):
        rc = ReadConfig()
        logname = rc.read("Log", "log_dir_name")
        filename = rc.read("Log", "file_name")
        projectname = rc.read("Log", "project_name")
        loglevel = int(rc.read("Log", "log_level"))
        logpath = os.path.abspath(os.path.dirname(os.getcwd())) + os.sep + logname
        if not os.path.isdir(logpath):
            os.mkdir(logpath)
        # 创建一个日志对象
        self.logg = logging.getLogger(projectname)
        # 定义一个模板
        FORMATTER = logging.Formatter('%(asctime)s|%(name)-12s: %(levelname)-8s %(message)s')
        # 创建一个屏幕流
        p_stream = logging.StreamHandler()
        # 创建一个文件流
        f_stream = logging.handlers.TimedRotatingFileHandler(logpath + os.sep + filename, when='D', backupCount=30)
        f_stream.suffix = "%Y-%m-%d_%H-%M-%S.log"
        # 将流绑定到模板
        p_stream.setFormatter(FORMATTER)
        f_stream.setFormatter(FORMATTER)

        # 将日志和流进行绑定
        self.logg.addHandler(p_stream)
        self.logg.addHandler(f_stream)
        # 设置日志记录等级
        self.logg.setLevel(loglevel)

    def debug(self, content):
        self.logg.debug(content)

    def info(self, content):
        self.logg.info(content)

    def warning(self, content):
        self.logg.warning(content)

    def error(self, content):
        self.logg.error(content)

    def critical(self, content):
        self.logg.critical(content)


if __name__ == '__main__':
    log = Log()
    log.debug("this is Debug")
    log.info("this is info")
    log.warning("this is warning")
    log.error("this is error")
    log.critical("this is critical")
