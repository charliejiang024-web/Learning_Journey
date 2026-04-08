import sys

n,m,k = map(int,input().split())

# 如果k（也就是球数小于n），则打印 -1

# 否则，先创建一个n * m的矩阵



# 先看看自己能不能打造一个 全部为0的矩阵

matrix = [[0] * 2 for _ in range(2)]
print(matrix)

# 把这个矩阵创造成功后如何填入内容
# 如何以斜角的方式填1到这个矩阵，再改其中一个1为 k - n 的数值