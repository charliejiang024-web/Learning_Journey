def log_dec(func): # 跟闭包有所不同，是传入一个函数而不再是一个参数
    def wrapper(*args,**kwargs):
        print("执行前")
        res = func(*args,**kwargs)
        print("执行后")
        return res
    return wrapper

@log_dec
def f():
    print("hello")

f()

# 打印日志，统计耗时，权限校验，参数检查
# 写一次就可以到处用，不会代码爆炸，难维护，一改全改

'''
程序设计铁律：对扩展开放，对修改关闭

别人写好的函数，你不能随便改源码
线上运行的函数，你不能乱动
库函数、三方函数，你根本改不了
'''

@log_dec
def login(): print('success')

@log_dec
def upload(): return 'uploaded'

@log_dec
def download(): return 'downloaded'

login()
upload()
download()
