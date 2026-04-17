import logging

# 说白了，还是记不住日志是怎么写出来的，而且还是不会用装饰器，学了半天没见效果
def get_logger(name='file_operation'):

    # 就记住大致的做法吧：每次先给logger命名
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    #第二步：logger的报警会有级别，这里info级别才会被记录
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    fh = logging.FileHandler('file_moving.log',encoding='utp-8')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

logger = get_logger()

def log_op(func):
    def wrapper(*args,**kwargs):
        logger.info(f"开始执行：{func.__name__}")
        result = func(*args,**kwargs)
        logger.info(f"执行完成: {func.__name__}")
        return result
    return wrapper



