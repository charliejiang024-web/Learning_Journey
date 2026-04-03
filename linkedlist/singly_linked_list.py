class ListNode: # 这个只是一个节点，还有一个类是装这些节点的
    def __init__(self,value):
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_tail(self,val):
        new_node = ListNode(val)
        # 如果列表为空，新节点就是头
        if not self.head:
            self.head = new_node
            return
        # 否则找到最后一个节点
        cur = self.head
        while cur.next:
            cur = cur.next
        # 把最后一个节点的next指向新节点
        cur.next = new_node

# 类似的还有打印整个列表
def print_list(self):
    cur = self.head
    # 指向头节点
    while cur:
        print(cur.val, end='->')
        cur = cur.next
    print("None")

