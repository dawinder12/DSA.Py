from collections import deque

queue = deque()

# Enqueue elements
queue.append(10)
queue.append(20)
queue.append(30)

print(queue)   # deque([10, 20, 30])

# Dequeue element
print(queue.popleft())  # 10

# Peek front
print(queue[0])         # 20
