import os
import logging

def get_logger():
    # 给这个日志取名字，叫 cleaner
    logger = logging.getLogger('cleaner')
    # 如果已有该日志，则不重复创建
    if logger.handlers:
        return logger

    # 日志有不同的级别，所以要先设置级别
    logger.setLevel(logging.INFO)

    # 设置完级别后要设置以什么形式输出
    fmt = "%(asctime)s | %(levelname)s | %(message)s"
    formatter = logging.Formatter()

    # stream handler 是在终端（控制台）输出
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    return logger


logger = get_logger()


def count_clean(func):
    # 这是外层的函数变量
    count = 0

    def wrapper(*args, **kwargs):
        # 内层函数
        # 在 内层函数里，只能读外部变量，不能直接改，所以需要这一行
        nonlocal count
        res = func(*args, **kwargs)
        # 然后才能对这个值进行修改
        count += 1
        logger.info(f"已删除文件累计：{count} 个")
        return res

    return wrapper
