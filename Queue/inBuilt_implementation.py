# USING LIST AS QUEUE (can use)
queue = []
# Enqueue items
queue.append(1) # or queue.insert(0, 1) and then while popping just do queue.pop()
queue.append(2) # or queue.insert(0, 2) and then while popping just do queue.pop()
queue.append(3)
# Dequeue items
print(queue.pop(0))  # Output: 1
print(queue.pop(0))  # Output: 2
print(queue.pop(0))  # Output: 3

# BY IMPORTING DEQUE FROM COLLECTIONS (Recommended)
from collections import deque
q = deque()
q.appendleft(5)
q.appendleft(8)
q.appendleft(27)
q.pop() # Output: 5
q.pop() # Output: 8
q.pop() # Output: 27

# BY IMPORTING QUEUE
import queue 
q = queue.Queue()
# Enqueue items
q.put(1)
q.put(2)
q.put(3)
# Dequeue items
print(q.get())  # Output: 1
print(q.get())  # Output: 2
print(q.get())  # Output: 3
