# 输入：
# 2,3,...,7
# 输出：
# 3

# sequence = input().split(',')
# count = 0
# first = int(sequence[0])
# last = int(sequence[-1])
# for i in range(first,last+1):
#     if str(i) not in sequence:
#         count += 1
# print(count)

# 算法过大，要找一个复杂度低一点的

sequence = input().split(',')
second = int(sequence[1])
last = int(sequence[-1])
tmp = last - second - 1
print(tmp)