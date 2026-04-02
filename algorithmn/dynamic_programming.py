# 动态规划的核心做法：
'''
1. 定义状态:dp[i] 表示到第i个位置的最优解
2. 定义状态转移方程,dp[i]和dp[i-1],dp[i-2]的关系是什么
3. 初始化:最底层的答案是什么
4. 确定遍历顺序:从底层开始，逐步向上计算
'''

#[0,1,1,2,3,5,8,13,21,34,55]
def fib(n):
    # 定义初始状态，ie当n等于最小数的时候会是什么样
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # 初始化dp数组
    dp = [0] * (n+1) # n + 1是为了和索引对齐
    dp[0] = 0
    dp[1] = 1

    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

m,m = 3,7


# 二维数组的动态规划解法：
def unique_paths(m,n):
    dp = [[0]*n for _ in range(m)]

    for j in range(n):
        dp[0][j] = 1
    for i in range(m):
        dp[i][0] = 1

    for i in range(1,m): # 这相当于是遍历了行
        for j in range(1,n): # 这相当于是遍历了列
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
    return dp[m-1][n-1]
            


    

