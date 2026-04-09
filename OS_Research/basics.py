import os

# print(os.getcwd()) # 现在的代码在哪个文件夹运行
# print('========================')
# print(os.listdir()) # 用一个列表列出当前目录下的所有文件
# print('========================')
# print(os.path.isfile('test.txt')) # 判断一个文件是否存在，exists则可以判断文件夹或者文件
# print('========================')
# # os.mkdir('a')
# os.makedirs('b/c',exist_ok=True)
#
# with open("new_file.txt", "w", encoding="utf-8") as f:
#     f.write("Hello World")

print(os.listdir(r'C:\Users\Administrator\Desktop\python\Foundamentals\automaic_trash_cleaner'))
# 得到的结果是一个列表，里面有 ['file_utils.py', 'logger_config.py', 'requirements.md', 'rules.py']

# 那如果有文件夹呢？
print(os.listdir(r'C:\Users\Administrator\Desktop\python\Foundamentals'))

'''
结果：['automaic_trash_cleaner', 'closure.py', 'decorator.py', 'files', 'functional_programming.py']
也就是说 是文件的会打出文件名+后缀，是文件夹的就打出文件夹的名字
'''

for name in (os.listdir(r'C:\Users\Administrator\Desktop\python\Foundamentals')):
    print(os.path.join(r'C:\Users\Administrator\Desktop\python\Foundamentals',name))

# 它实际上就是把这些文件的全部路径一一输出出来