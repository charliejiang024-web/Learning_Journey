import logging
from utils.logger import setup_logger
from database import get_user

# 主程序 logger
logger = setup_logger(
    name="main",
    log_file="main.log",
    level=logging.DEBUG
)

def main():
    logger.info("程序启动")

    user = get_user(100)
    logger.info(f"获取用户结果: {user}")

    user2 = get_user(-5)
    logger.warning(f"错误用户获取失败: {user2}")

    logger.info("程序结束")

if __name__ == '__main__':
    main()