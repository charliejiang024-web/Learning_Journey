string = input()
# 首先建立一个字典.去查每个字母的出现次数
dic = {}
for let in string:
    if let in dic:
        dic[let] += 1
    else:
        dic[let] = 1
# 这样就找到了字母的出现次数
print(min(i for i in dic.values()))
# 得delete掉所有出现次数最少的字母
# 其实一段python代码就可以解决：
string = ''.join([let for let in string if dic[let] != min(i for i in dic.values())])
print(string)