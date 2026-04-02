n = 4

# 初始化 一个 n * n 的矩阵，全部填0

mat = [[0] * n for _ in range(n)]

num = 1

# 第一层，控制填几条斜线
for s in range(1,n+1):
    row = s - 1
    col = 0
# 其实就相当于你控制要填写多少内容，里面的数字暂时是不管的

# 然后在这些内容的基础上填数字，所以是一个嵌套 loop
    for _ in range(s):
        mat[row][col] = num # 从一开始
        num += 1 #分别填写2,3,4,5等
        # 行和列都已经在第一层列好了，所以可以直接用
        # 根据规律，第二行第一个数字是2，第一行第二个数字是3，所以
        row -= 1
        col += 1
        # 这个的先后顺序是先填了1，然后再往右上角去走，所以第一行第二个就成了2

for line in mat:
    print(' '.join(map(str,line)))




