import os

print(os.getcwd()) # 现在的代码在哪个文件夹运行
print('========================')
print(os.listdir()) # 用一个列表列出当前目录下的所有文件
print('========================')
print(os.path.isfile('test.txt')) # 判断一个文件是否存在，exists则可以判断文件夹或者文件
print('========================')
# os.mkdir('a')
os.makedirs('b/c',exist_ok=True)

with open("new_file.txt", "w", encoding="utf-8") as f:
    f.write("Hello World")
