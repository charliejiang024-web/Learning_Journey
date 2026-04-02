n = int(input())
dic = {}
for _ in range(n):
    inp = input().strip().split()
    a, b = int(inp[0]), int(inp[1])
    # 找到相同的a并相加b
    # dic[a] = b 这是不对的，第二个相同的索引的值会被覆盖
    # dic[a] 实际上是取到值，就可以用来相加减
    if a in dic:
        dic[a] += b # 这个其实就是把与a键相同的值配对上了
    else:
        dic[a] = b
# 在形成这样一个字典后就可以进行从小到大进行排序
sorted_keys = sorted(dic)
# 遍历排序后的键，输出键值对

#对字典再次进行一个复习，键是什么值是什么，怎么应用
for key in sorted_keys:
    print(key, dic[key])
    
