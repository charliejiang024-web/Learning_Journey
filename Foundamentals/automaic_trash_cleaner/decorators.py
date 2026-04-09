def safe_confirm(func):
    def wrapper(*args,**kwargs): # 这两个参数可以灵活控制接收（多个参数），而不是一个
        res = input("确定删除？y/n")
        if res != 'y':
            return
        return func(*args,**kwargs)
    return wrapper