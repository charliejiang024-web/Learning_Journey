
n, m, k = map(int, input().strip().split()) # 这段代码把n，m，k转化成整数

if k < max(n, m): # 这个也好理解，每行每列都要有至少一个1，之所以用max是因为不知道是列还是行大
    # 我理解错误的地方是在于默认这是一个方形矩阵，事实上n和m可能会不一样
    print(-1)
else:
    # 这里我也是直接把0当成整数放进去了，实际上应该是字符串
    res = [['0'] * m for i in range(n)]
    cur = 0
    while cur < max(n, m): # 这个是看是行还是列多，取数多的那个
        if cur < min(n, m): # 这里就很有学问了，因为我们是填对角线，所以n和m谁最小我们就按照最小的那个填方形矩阵的对角线
            res[cur][cur] = '1'
            cur += 1
            k -= 1
        else:
            # 这里它也分情况讨论了，如果1还填不完，就看m大还是n大，大的那个填上1
            if m > n:
                res[0][cur] = '1'
            else:
                res[cur][0] = '1'
            k -= 1
            cur += 1
    if k > 0:
        res[0][0] = str(int(res[0][0]) + k)
    for _ in res:
        print(' '.join(_))

