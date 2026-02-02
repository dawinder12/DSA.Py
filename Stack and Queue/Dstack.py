from collections import deque

stack = deque()

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)   # deque([10, 20, 30])

# Pop element
print(stack.pop())  # 30

# Peek top
print(stack[-1])    # 20
