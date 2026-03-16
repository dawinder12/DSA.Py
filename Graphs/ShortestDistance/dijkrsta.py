import heapq
class Solution:
    # Returns shortest distances from src to all other vertices 

    def dijkstra(self, V, edges, src):
        adj = [[] for _ in range(V)]
        distance = [-1] * V

        for u, v, d in edges:
            adj[u].append((v, d))
            adj[v].append((u, d))

        queue = []
        heapq.heappush(queue, (0, src))
        distance[src] = 0

        while len(queue) > 0:
            dist, node = heapq.heappop(queue)
            if dist > distance[node]:
                continue
            for nei, diff in adj[node]:
                if distance[nei] == -1:
                    distance[nei] = dist + diff
                    heapq.heappush(queue, (dist + diff, nei))
                else:
                    if dist + diff < distance[nei]:
                        distance[nei] = dist + diff
                        heapq.heappush(queue, (dist + diff, nei))

        return distance
            
            