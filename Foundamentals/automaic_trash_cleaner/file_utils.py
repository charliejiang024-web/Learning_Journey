import os
from rules import is_trash
from decorators import count_deleter
from logger_config import get_logger

logger = get_logger("file_ops")

# 暂时注释 safe_confirm，避免卡住
# @safe_confirm
@count_deleter
def delete_single_file(file_path):
    os.remove(file_path)
    logger.info(f"[删除] {file_path}")

def scan_and_clean(folder_path, recursive=True):
    if not os.path.isdir(folder_path):
        logger.warning(f"不是目录：{folder_path}")
        return

    for name in os.listdir(folder_path):
        full_path = os.path.join(folder_path, name)

        # 是目录 → 递归
        if os.path.isdir(full_path):
            if recursive:
                scan_and_clean(full_path, recursive=True)
            continue

        # 是文件 → 判断垃圾
        if is_trash(full_path):
            logger.debug(f"匹配垃圾文件：{full_path}")
            delete_single_file(full_path)