# ascii_code = ord('A')

# print(ascii_code)
# print(chr(ascii_code+1))

inp = 'abcabcD'

# 暴力解法：枚举所有从a开始到第二个a的子段，找出长度最小的那个并打印出来
count = 0 # 去计算a到了第几个
lst = []
for let in inp:
    if let == 'a':
        count += 1
        start = inp.index(let)
        if count == 2:
            end = inp.index(let)
            count = 0
        lst.append(inp[start:end+1])
print(lst)

