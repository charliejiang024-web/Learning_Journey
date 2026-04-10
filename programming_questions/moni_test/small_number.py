

'''
给出一个数字n，有三种操作：
 1）如果n为0或者正数，开根号，也就是  if (n ** 0.5) is not int, n = n** 0.5 + 1, else n
2) n -1
3) n // 2，跟1）一样的逻辑： if (n // 2) is not int, n = n // 2 + 1, else n
数字 n 可以操作 m 次，问m次后n最小为多少

输入：第一行给出多少个数组
第二行和之后给出n m
'''

t = int(input())
for line in range(t-1):
    n,m = map(int,line.split())

#过一段时间自己再想想，其实不复杂