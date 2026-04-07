import logging
from utils.logger import setup_logger

logger = setup_logger(
    name=__name__,
    log_file='db.log',
    level=logging.INFO
)

def get_user(user_id):
    logger.info(f"查询用户 ID: {user_id}")

    if user_id <= 0:
        logger.error(f"用户ID不合法: {user_id}")
        return None

    logger.debug(f"内部细节：正在拼接SQL语句")  # 文件里会有，控制台没有
    return {"id": user_id, "name": "测试用户"}