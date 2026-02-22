import heapq

# Create empty heap
pq = []

# Insert elements (Push)
heapq.heappush(pq, 10)
heapq.heappush(pq, 5)
heapq.heappush(pq, 20)

print(pq)  # Internal heap structure (not sorted!)

# Remove smallest element (Pop)
smallest = heapq.heappop(pq)
print("Removed:", smallest)

# Peek smallest element
print("Top element:", pq[0])