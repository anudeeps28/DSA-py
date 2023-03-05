# USING LISTS
class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        
    def is_empty(self):
        return len(self.items) == 0
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def size(self):
        return len(self.items)

# USING DEQUE FROM COLLECTIONS
from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()
        
    def push(self, item):
        self.container.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.container.pop()
        
    def is_empty(self):
        return len(self.container) == 0
        
    def peek(self):
        if not self.is_empty():
            return self.container[-1]
        
    def size(self):
        return len(self.container)