import logging

def get_logger(name=__name__):
    logger = logging.getLogger("cleaner")
    # 防止重复添加 handler
    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    # 日志格式
    fmt = "%(asctime)s | %(name)-12s | %(levelname)-8s | %(message)s"
    formatter = logging.Formatter(fmt)

    # 控制台输出
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    return logger