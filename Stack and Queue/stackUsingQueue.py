# from collections import deque

# class MyStack:
#     def __init__(self):
#         self.queue = deque()  # Single queue
    
#     def push(self, x: int) -> None:
#         self.queue.append(x)  # Add to end
#         # Rotate: move front elements to end (len-1 times)
#         for _ in range(len(self.queue) - 1):
#             self.queue.append(self.queue.popleft())
    
#     def pop(self) -> int:
#         return self.queue.popleft()  # Remove front (top)
    
#     def top(self) -> int:
#         return self.queue[0]  # Peek front
    
#     def empty(self) -> bool:
#         return len(self.queue) == 0  # Check if empty


from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()  # Main queue
        self.q2 = deque()  # Helper queue
    
    def push(self, x: int) -> None:
        self.q2.append(x)  # Add new element to helper
        # Move all from main to helper
        while self.q1:
            self.q2.append(self.q1.popleft())
        # Swap: helper becomes main
        self.q1, self.q2 = self.q2, self.q1
    
    def pop(self) -> int:
        return self.q1.popleft()  # Remove front (top of stack)
    
    def top(self) -> int:
        return self.q1[0]  # Peek front
    
    def empty(self) -> bool:
        return len(self.q1) == 0  # Check if main is empty