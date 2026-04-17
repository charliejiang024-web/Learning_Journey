import re

with open('test.txt','r',encoding='utf-8') as f:
    text = f.read()


# # print(text)
# result = re.findall(r'\d',text) # 匹配0-9任意一个数字
# print(r"这是用r'\d'获得的 {}".format(result))
# #输出 ['1', '0', '0', '2', '0',etc],就是一个列表里面包含了单个的字符串数字
# print('===========================================================================')
# result1 = re.findall(r'\d+',text)
# print(result1) # 匹配连续数字
# print('===========================================================================')
# result2 = re.findall(r'\w+', text)
# print(result2) # 匹配字母，数字，下划线
# print('===========================================================================')
# # a 后面随便一个字符
# result3 = re.findall(r'a.', text) # . 其实就是一个字符
# print(result3)
# # 匹配任意一个字符
# # ['ap', 'an', 'an', 'a ', 'at', 'ai', 'ai', 'ab']
# print('===========================================================================')
# # a 开头，后面随便
# result4 = re.findall(r'a.*', text) # * 是匹配0次或多次
# print(result4) # 匹配0次或多次
# print('===========================================================================')
# result5 = re.findall(f'^IP:.*',text,flags=re.MULTILINE)
# print(result5)

# 假设我要发现在文件当中的邮箱
result = re.findall(r"\w+@\w+\.com",text)
print(result)

# 要发现在文件中的网址
web = re.findall(r"http://www\.\w+\.com\.cn|http://www\.\w+\.com",text)
print(web)
# ['http://www.abc.com', 'http://www.abc.com'] .cn没有匹配上去

# s 可有可无, 括号是看做一个整体
web_advanced = re.findall(r"https?://www\.\w+\.\w+(?:\.\w+)?",text)
print(web_advanced)