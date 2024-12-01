# Stacks - Last in First Out (Lifo)

stk = []
print(stk)

# Append to top of stack - O(1)
stk.append(5)

stk.append(4)
stk.append(3)

stk

# Pop from stack - O(1)
x = stk.pop()

print(x)
print(stk)

# Ask what's on the top of stack - O(1)
print(stk[-1])

# Ask if something is in the stack - O(1)
if stk:
  print(True)

# Queues - First in First out (Fifo)

from collections import deque

q = deque()

print(q)

# Enqueue - Add element to the right - O(1)
q.append(5)
q.append(6)
q.append(7)
q

# Deqeue (pop left) - Remove element from the left - O(1)
q.popleft()

q

# Peek from left side - O(1)
q[0]

# Peek from right side - O(1)
q[-1]