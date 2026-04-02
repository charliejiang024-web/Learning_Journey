inp = input()
total_len = len(inp)

# 不是先计算要补几个0，而是直接遍历字符串，按步长8遍遍历
for start in range(0, total_len, 8):
    # 这个是干什么，从0开始遍历，一直到第8个字符
    # 这个时候取sub_string，而不是一开始就定义这个常量
    sub_str = inp[start:start+8] # 这是相当于把 这个字段截取并赋值给了sub_str
    need_pad = 8 - len(sub_str)
    if need_pad > 0:
        sub_str += '0' * need_pad
    print(sub_str)