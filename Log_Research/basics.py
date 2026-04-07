import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename='app.log',
    filemode='a',
    encoding='UTF-8'
)

logging.debug("调试信息")
logging.info("普通信息")
logging.warning("警告")
logging.error("报错")
logging.critical("严重错误")

