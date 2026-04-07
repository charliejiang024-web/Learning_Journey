import os

def trash_cleaner(path):
    for file in os.listdir(path):
        full_path = os.path.join(path,file)
        # 找到这个目录里的文件之后要判断是否是文件
        if os.path.isfile(full_path):
            # 判断是否以 .log 结尾
            if file.endswith(".log"):
                print("正在删除：", full_path)
                os.remove(full_path)



if __name__ == '__main__':
    trash_cleaner('C:/Users/Administrator/Desktop/python/OS_Research/a')