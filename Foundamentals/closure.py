'''
闭包
函数嵌套，内层函数引用外层函数的变量，外层函数返回内层函数
'''

# 保留状态，封装变量，做装饰器的基础

def outer(x):
    def inner(y):
        return x + y
    return inner

add5 = outer(5)
print(add5(3))