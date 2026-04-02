# string = 'hellonowcoder' 
# n = len(string)
# # 我的错误代码：
# for i in range(0,n,8):# 这个的意思是从索引0开始，每次跳8个字符
#     # 截取的问题
#     tmp = string[0:n] # 我是直接把所有的字符都截取了
#     # print(tmp)
#     '''得出两个 hellonowcoder
#     hellonowcoder'''
#     # 那这样有什么意义呢？不如直接print 这个乘以 2
#     # 所以，截取的时候必须严谨的指定开始索引和结束索引，在这个例子中

# # 正确的写法：
# for start in range(0,n,8):
#     # 其实这里叫tmp是不严谨的，应该叫sub_str
#     sub_str = string[start:start+8]
#     print(sub_str)
#     # 当start=0时候，start+8就是8，所以截取的是从0到8的字符
#     # 然后判断是否需要补0

        

'''
4
0 1
0 2
1 2
3 4
'''



