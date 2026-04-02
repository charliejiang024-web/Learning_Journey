# # 20
# # 9 9 6 7 9 5 2 2 6 6 4 1 3 7 5 8 3 1 8 4
# a = list(map(int, input().split()))
#
# count = [0] * 10
# for num in a:
#     count[num] += 1
#     # 这样我们就得到了每个数字出现次数的统计，比如数字1在索引1出现了两次
#
# standard = count[1]
#
# valid = True
# for i in range(2,10):
#     if count[i] != standard:
#         valid = False
#         break
# print("Yes" if valid else "NO")
#
#











# 用列表判断出现次数 9 9 6 7 9 5 2 2 6 6 4 1 3 7 5 8 3 1 8 4

n = 20
nums = map(int,input().split())
# 先创造一个列表, 使得这20个值为0
lst = [0 for _ in range(n)]
for num in nums:
    lst[num] += 1
print(lst)


















