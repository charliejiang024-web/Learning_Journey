'''
在文件的工具里，我们首先需要知道一个 path（路径）有哪些文件
'''

import os
from rules import is_trash
from decorators import safe_confirm

def list_all_files(path):
    for name in os.listdir(path):
        full = os.path.join(path,name)
        print(full)

@safe_confirm
def delete_file(filepath):
    os.remove(filepath)
    print("删除：", filepath)

def scan_files(path):
    for name in os.listdir(path):
        full = os.path.join(path,name)
        if os.path.isdir(full): # 如果说这个路径是一个文件夹的话
            scan_files(path)
        else:
            if is_trash(name):
                delete_file(full)




