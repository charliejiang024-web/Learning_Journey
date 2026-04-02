def simple_decorator(data):
    def wrapper():
        print("准备执行函数", data.__name__)
        result = data()
        return result
    return wrapper

@simple_decorator
def say_hello():
    print("Hello,装饰器!")
    return "函数执行完成"
    
result = say_hello()
print(result)

