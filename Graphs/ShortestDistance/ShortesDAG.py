from collections import deque
from typing import List

class Solution:
    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        
        adj = [[] for _ in range(V)]
        distance = [-1] * V

        for u, v, d in edges:
            adj[u].append((v, d))

        queue = deque()
        src = 0
        queue.append((src, 0))
        distance[src] = 0

        while len(queue) > 0:
            node, dist = queue.popleft()

            for nei, diff in adj[node]:
                if distance[nei] == -1:
                    distance[nei] = dist + diff
                    queue.append((nei, dist + diff))
                else:
                    if dist + diff < distance[nei]:
                        distance[nei] = dist + diff
                        queue.append((nei,dist+diff))
        return distance