# encoding:utf-8

import logging
import sys

SWITCH = True

def _get_logger():
    log = logging.getLogger('log')
    log.setLevel(logging.INFO)
    console_handle = logging.StreamHandler(sys.stdout)
    console_handle.setFormatter(logging.Formatter('[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d] - %(message)s',
                                                  datefmt='%Y-%m-%d %H:%M:%S'))
    log.addHandler(console_handle)
    return log

def close_log():
    global  SWITCH
    SWITCH = False


def debug(arg, *args):
    if SWITCH:
        if args:
            logger.debug(arg.format(*args))
        else:
            logger.debug(arg)

def info(arg, *args):
    if SWITCH:
        if args:
            logger.info(arg.format(*args))
        else:
            logger.info(arg)


def warn(arg, *args):
    if not args:
        logger.warning(arg)
    else:
        logger.warning(arg.format(*args))

def error(arg, *args):
    if not args:
        logger.error(arg)
    else:
        logger.error(arg.format(*args))

def exception(e):
    logger.exception(e)


# 日志句柄
logger = _get_logger()
