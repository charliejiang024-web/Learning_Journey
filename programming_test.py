dic = {
    'b': 2,
    'c': 3,
    'd': 2,
    'a': 5
}

# print(sorted(dic,key=lambda i:(-dic[i],i)))

s = input()
# 计算需要补充 0 的个数：
# 这是你设置的一个规则
if len(s) % 8 != 0: # 13-8 = 5,也就是说要pad五个0，所以有以下公式
    add_0_num = '0' * (8 - len(s) % 8)
else:
    add_0_num = 0
# 知道了要pad几个0后就可以开始给原字符串补0了
s_padding = s + add_0_num # 这样就很巧妙的知道了要补几个0并补上

# 然后遍历这个补0后的字符串，每次取8个字符输出
for i in range(0, len(s_padding), 8):
    segment = s_padding[i:i+8] # 这个叫做截取，因为实际上for遍历什么也没做，只是规定了每8个字符输出一次

    print(segment)
