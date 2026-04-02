# a能被b整除
a % b == 0

# 偶数的意思是能被 2 整除，奇数的意思是被2整除后等于1
num % 2 == 1 # 奇数

# 约数是能整除n的数，比如说n=12，它的约数有1,2,3,4,6,12

'''
质数是大于1的自然数,除了1和自身外无其他约数
'''

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True 

# 要生成一个<= n的所有数字

#用埃氏筛法
def generate_primes(n):
    if n < 2:
        return []
    # 首先生成一个 is_prime 数组，用来记录每个数是否是质数
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False #设置索引0和1为False
    for i in range(2,int(n**0.5)+1): # 遍历所有小于等于n的平方根的数
        if is_prime[i]: # 如果是质数
            is_prime[i*i : n+1 : i] = [False] * len(is_prime[i*i : n+1 : i])
    primes = [i for i,val in enumerate(is_prime) if val]













# python的round不是四舍五入，0.5的时候偶数是向上奇数是向下

# 答案的做法：
num = float(input())
integer_part = int(num) # 提取整数部分，这个也是我会的
# 我是傻逼：
decimal_part = num - integer_part
# 这里直接给一个变量，然后再判断不就可以了
if decimal_part >= 0.5:
    print(integer_part+1)
else:
    print(integer_part)