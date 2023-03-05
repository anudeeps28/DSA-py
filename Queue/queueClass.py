from collections import deque

# using lists
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items.pop(0)

    def size(self):
        return len(self.items)

# using deque from collections
class Queue:
    def __init__(self):
        self.buffer = deque()

    def is_empty(self):
        return len(self.buffer) == 0

    def enqueue(self, item):
        self.buffer.appendleft(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items.pop()

    def size(self):
        return len(self.buffer)



