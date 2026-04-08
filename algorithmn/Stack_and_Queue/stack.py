class Stack:
    def __init__(self):
        self.stack = []

    # 入栈操作叫push，出栈叫pop
    def push(self, value):
        self.stack.append(value)
        return self.stack

    def is_empty(self):
        return len(self.stack) == 0
    
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
    
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value): # 对于队列，入队操作叫enqueue，出队操作叫dequeue
        self.queue.append(value)
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop() # pop 默认尾部取出
    