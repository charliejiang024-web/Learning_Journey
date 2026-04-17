from file_utils import scan_and_clean
from logger_config import get_logger

logger = get_logger("main")

if __name__ == "__main__":
    logger.info("开始垃圾清理")
    scan_and_clean(r"C:\Users\Administrator\Desktop\python\Foundamentals\files", recursive=True)
    logger.info("清理结束")