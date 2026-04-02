# 单项列表问题
# 第一行输入有几个节点
# 第二行输入节点
# 第三行输入需要倒数第几个节点

class ListNode:
    def __init__(self, val):
        self.val = val          # 对应 int val
        self.m_pNext = None    # 对应 ListNode* m_pNext
'''
输入：
3
1 2 3
1
8
1 2 3 4 5 6 7 8
4
'''

# 因为input.split()是个数组，所以要根据数组创建列表
# 这是第一个需求，所以要有一个函数来实现它
def create_linked_list(arr):
    dummy = ListNode() # 刚开始一般都要有个虚拟节点
    current = dummy

    for num in arr:
        current.m_pNext = ListNode(num)
        current = current.m_pNext
    # 看起来好像是把所有节点去跟这个dummy_node接上了
    return dummy.mp_Next
# 这样就顺利的把这些节点接成一个单向列表了

# 那有了这些节点后就可以找倒数第几个节点了

def find_kth_from_end(head,k): # 这个head就是我们之前解析的那些节点
    # 首先我们要知道这个链表的长度
    # 因为不能像列表一样直接用len，得过一遍这个链表
    length = 0
    cur = head
    # 先用一个指针cur指向头部节点
    while cur:
        length += 1
        cur = cur.m_pNext
    cur = head
    for _ in range(length - k):
        cur = cur.m_pNext
    return cur.val

import sys

def main():
    # 如何地去把每一行input都转为一个包含字符串的列表
    lines = [line.strip() for line in sys.stdin if line.strip()]
    idx = 0
    while idx < len(lines): # 当命令行输入还没有结束
        # 分个 解析每个命令行
        n = int(lines[idx])
        idx+=1

        arr = list(map(int,lines[idx].split()))
        idx +=1

        k = int(lines[idx])
        idx += 1

        head = create_linked_list(arr)
    



