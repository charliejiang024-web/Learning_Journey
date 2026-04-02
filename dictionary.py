from collections import defaultdict
from collections import Counter
# 构造字典的第一种方式
dict1 = {'name':'james','age':18}
# 构造字典的第二种方式：
dict2 = dict(name='alen',age=20) # 关键字参数
dict3 = dict([('name','kate'),('age',22)]) # 可迭代对象

import copy
d = {"a": 1, "b": [2, 3]}
d_shallow = d.copy()
d_deep = copy.deepcopy(d)
# 在 d改变时，deepcopy不会变
d["b"].append(4)
print("这是shallow_copy: ", d_shallow)
print("这是deep_copy:", d_deep)

a = defaultdict(list)
a['name'].append('pork')
a['age'].append(None)
print(a)

b = defaultdict(int)
for i in "we shall never give up":
    b[i] += 1
print(b)



