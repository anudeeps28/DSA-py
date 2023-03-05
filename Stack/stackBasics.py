# USING LIST AS A STACK (can use)
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)  # Output: [1, 2, 3]
print(stack.pop()) # Output: 3; also removes 3 from the stack
print(stack.pop()) # Output: 2; also removes 2 from the stack
print(stack.pop()) # Output: 1; also removes 1 from the stack
print(stack)  # Output: []

# there is no .top()/.peek() methods in python stack; 
# use the "-1th" index access the "top" (value inserted at the last) value
stack = [1, 2, 3]
top_element = stack[-1]
print(top_element)  # Output: 3

######################################################################

# USING COLLECTIONS DEQUE AS STACK (Recommended)
from collections import deque
stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)

stack.pop() # Output: 1
stack.pop() # Output: 2
stack.pop() # Output: 3



