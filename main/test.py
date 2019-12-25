import logging
import os
from logging import handlers


def _logging(**kwargs):
    level = kwargs.pop('level', None)
    filename = kwargs.pop('filename', None)
    datefmt = kwargs.pop('datefmt', None)
    format = kwargs.pop('format', None)
    if level is None:
        level = logging.DEBUG
    if filename is None:
        filename = 'default.log'
    if datefmt is None:
        datefmt = '%Y-%m-%d %H:%M:%S'
    if format is None:
        format = '%(asctime)s [%(module)s] %(levelname)s [%(lineno)d] %(message)s'

    log = logging.getLogger(filename)
    format_str = logging.Formatter(format, datefmt)

    def namer(filename):
        return filename.split('default.')[1]

    # cmd = logging.StreamHandler()
    # cmd.setFormatter(format_str)
    # cmd.setLevel(level)
    # log.addHandler(cmd)

    os.makedirs("./debug/logs", exist_ok=True)
    th_debug = handlers.TimedRotatingFileHandler(filename="./debug/" + filename, when='D', backupCount=3,
                                                 encoding='utf-8')
    # th_debug.namer = namer
    th_debug.suffix = "%Y-%m-%d.log"
    th_debug.setFormatter(format_str)
    th_debug.setLevel(logging.DEBUG)
    log.addHandler(th_debug)

    th = handlers.TimedRotatingFileHandler(filename=filename, when='D', backupCount=3, encoding='utf-8')
    # th.namer = namer
    th.suffix = "%Y-%m-%d.log"
    th.setFormatter(format_str)
    th.setLevel(logging.INFO)
    log.addHandler(th)
    log.setLevel(level)
    return log


os.makedirs('./logs', exist_ok=True)
logger = _logging(filename='./logs/default')
logger.error("hhhh")