import logging
import os

def setup_logger(
        name=__name__,
        log_file='app.log',
        level=logging.INFO,
        fmt="%(asctime)s | %(name)-12s | %(levelname)-8s | %(message)s"
):
    """
        可自定义的日志配置函数
        :param name: logger 名字
        :param log_file: 日志文件名
        :param level: 日志级别
        :param fmt: 日志格式
        """
    # 1. 获取 logger 对象
    logger = logging.getLogger(name)

    # 防止重复添加 handler（多次调用不重复输出）
    if logger.handlers:
        return logger

    # 2. 设置最低级别
    logger.setLevel(logging.DEBUG)  # 全局最低设为DEBUG，不漏信息

    # 3. 创建格式器
    formatter = logging.Formatter(fmt)

    # 4. 输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)  # 控制台用传入的级别
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # 5. 输出到文件
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)  # 文件记录所有级别
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger