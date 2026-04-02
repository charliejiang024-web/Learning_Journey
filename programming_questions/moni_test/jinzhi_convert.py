# print(bin(20)) # 这是十进制转二进制

# 如果要把一个十六进制转换为10进制，则可以加一个参数
#print(int('0b10100', ))

n = int(input())
m = int(input())
bin_n = bin(n)
bin_m = bin(m)
print(len([i for i in bin_n if i == '1']))
print(len([j for j in bin_m if j == '1']))