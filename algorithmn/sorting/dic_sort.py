# 了解 dic.items() 的底层逻辑

count = {'a': 2, 'b': 1, '3': 2}

print(count.items())

'''
输出的内容是dict_items([('a', 2), ('b', 1), ('3', 2)])
其实就是一个tuple（元组）
'''

print(sorted(count.items()))

'''
输出的内容是[('3', 2), ('a', 2), ('b', 1)]
所以如果我们指定x，那么这里的每一对就会被拿出来
'''
print(sorted(count.items(),key=lambda x: (-x[1],x[0])))

