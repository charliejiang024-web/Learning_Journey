def para(func):
    def wrapper(*args,**kwargs):
        print("准备执行函数", func.__name__)
        result = func(*args,**kwargs)
        print("函数返回值是 {}".format(result))
        return result
    return wrapper

@para
def add(a,b):
    return a+b

@para
def hello(name):
    return "你好，{}".format(name)

add(1,2)
hello("张三")



