# 判断是不是垃圾

def is_trash(filename):
    return filename.endswith(('.log', '.tmp', '.bak'))