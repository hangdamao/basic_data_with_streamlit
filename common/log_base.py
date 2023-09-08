import logging
from logging.handlers import RotatingFileHandler
from common.tools import project_dir
from pathlib import Path


def config_flask_log():
    # 设置日志的的登记
    logging.basicConfig(level=logging.INFO)
    # 日志输出目录
    log_path = Path(project_dir(), 'logs', 'run.log')
    # 创建日志记录器，设置日志的保存路径和每个日志的大小和日志的总大小
    file_log_handler = RotatingFileHandler(log_path, encoding='UTF-8', maxBytes=1024 * 1024 * 100, backupCount=100)
    # 创建日志记录格式，日志等级，输出日志的文件名 行数 日志信息
    formatter = logging.Formatter(
        "%(levelname)s | %(asctime)s | %(filename)s | %(funcName)s: %(lineno)s | : %(message)s")
    # 为日志记录器设置记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flaks app使用的）加载日志记录器
    logging.getLogger().addHandler(file_log_handler)
