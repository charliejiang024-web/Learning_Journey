import sys

inp = [line.strip() for line in sys.stdin if line.strip()]
idx = 0
while idx < len(inp):
    # 读取输入
    n = int(inp[idx])
    idx += 1

    candidates = inp[idx].split()
    idx += 1

    m = int(inp[idx])
    idx += 1

    votes = inp[idx].split()
    idx += 1

    # ======================
    # 统计票数（优雅写法）
    # ======================

    # 字典也可以用合并写法，这个还要多练习

    result = {name:0 for name in candidates}
    result["Invalid"] = 0

    for v in votes:
        if v in result:
            result[v] += 1
        else:
            result["Invalid"] += 1

    # ======================
    # 严格按题目格式输出
    # ======================
    for name in candidates:
        print(f"{name} : {result[name]}")

    print(f"Invalid : {result['Invalid']}")