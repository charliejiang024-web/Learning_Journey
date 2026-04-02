s = 'Nowcoder Hello'

# 遍历这个字符串，如果碰到的字符不是字母，则记录到一个列表中
lst = []
string = ''
for char in s:
    if char.isalpha():
        string += char
    else:
        pass