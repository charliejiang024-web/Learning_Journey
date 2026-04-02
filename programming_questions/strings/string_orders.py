'''对于给定的由可见字符和空格组成的字符串，按照下方的规则进行排序：
∙按照字母表中的顺序排序（不区分大小写）；
∙同一字母的大小写同时存在时，按照输入顺序排列；
∙非字母字符保持原来的位置不参与排序；
直接输出排序后的字符串。'''
letters = input()
tmp = []
for let in letters:
    if let.isalpha():
        tmp.append(let)
# 把字母提出来，后面只需要对字母排序
# sorted 函数只能按照一个值比大小（如数组，字符串），规则声明“忽略大小写”
# 所以需要先把字母都转换为小写或者大写，再排序
def sort_key(char):
    lower_char = char.lower() 
    is_lower = 1 if char.islower() else 0
    return (lower_char, is_lower)

tmp_sorted = sorted(tmp, key=sort_key) # 这样就可以按照忽略大小写，同字母时大写在前

# 重建字符串
result = []
idx = 0
for char in letters:
    if char.isalpha():
        result.append(tmp_sorted[idx])
        idx += 1
    else:
        result.append(char)
