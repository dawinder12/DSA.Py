from collections import deque
from copy import deepcopy

class Solution:
    def shortestPath(self, V, adj, src):
        distance = [-1] * V
        graph = deepcopy(adj)
        adj = [ [] for _ in range(V)]
        for u,v in graph :
            adj[u].append(v)
            adj[v].append(u)
        queue =deque()
        queue.append((src,0))
        distance[src] = 0
        while len(queue) > 0 :
            node,dist = queue.popleft()
            for nei in adj[node]:
                if distance[nei] == -1 :
                    distance[nei] = dist + 1
                    queue.append((nei,dist + 1))
                else :
                    if dist + 1 < distance[nei]:
                        distance[nei] += 1
                        queue.append((nei,dist+1))
        return distance