# 4
# A B C D
# 8
# A D E CF A GG A B

import sys
inp = [lines.strip() for lines in sys.stdin if lines.strip()]
idx = 0
while idx < len(inp):
    n = int(inp[idx])
    idx += 1

    eligible_voters = inp[idx].split()
    idx += 1

    m = int(inp[idx])
    idx += 1

    voters = inp[idx].split()
    idx += 1

    # 先想好思路：
    '''
    1. 把无效票去掉并用字典统计
    1.1: 如果在voters里的选民不在eligible voters里，则统计无效票
    2. 用字典统计每个人的票数
    '''

    votes = {'Invalid': 0}
    for voter in voters:
        votes[voter] = 0
    for voter in voters:
        if voter in eligible_voters:
            votes[voter] += 1
        else:
            votes['Invalid'] += 1

    print(votes)

