# 学习 python map, reduce 函数

from functools import reduce

lst = list(range(51))

# print(list(map(lambda x:x*5, lst)))

# print(reduce(lambda x,y:x+y, lst))

def use_filter(num):
    return num % 2 == 0



