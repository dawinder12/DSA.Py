#becuase mentioned no -ve w so we used dijkrsta instead of floyd warhsall

import heapq

class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        # 1. Build the Adjacency List ONLY (Do NOT pre-fill the distance matrix with weights)
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
            
        # 2. Initialize the distance matrix with infinity
        distance = [[float("inf") for _ in range(n)] for _ in range(n)]
        
        # 3. Run Dijkstra from every node
        for start in range(n):
            distance[start][start] = 0
            p_queue = [(0, start)] # (current_distance, current_node)
            
            while p_queue:
                dist, node = heapq.heappop(p_queue)
                
                # STANDARD OPTIMIZATION: Skip stale, outdated paths in the queue
                if dist > distance[start][node]:
                    continue
                    
                # Explore neighbors
                for nei, w in adj[node]:
                    new_dist = dist + w
                    
                    # STANDARD CONDITION: Only process if we found a strictly shorter path
                    if new_dist < distance[start][nei]:
                        distance[start][nei] = new_dist
                        heapq.heappush(p_queue, (new_dist, nei))
                        
        # 4. Find the city with the smallest number of reachable neighbors
        city = -1
        min_reachable = float("inf")
        
        for i in range(n):
            reachable_count = 0
            for j in range(n):
                if i != j and distance[i][j] <= distanceThreshold:
                    reachable_count += 1
            
            # The <= naturally handles the tie-breaking rule to return the greatest city ID
            # because we iterate from 0 to n-1. Later 'i's overwrite earlier ones if counts are equal.
            if reachable_count <= min_reachable:
                min_reachable = reachable_count
                city = i
                
        return city