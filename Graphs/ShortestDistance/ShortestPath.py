from typing import List
import heapq
class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        # code here
        adj = [[] for _ in range(n+1)]
        for u,v,w in edges :
            adj[u].append((v,w))
            adj[v].append((u,w))
        parent = [-1] * (n+1)
        distance = [float("inf")] * (n+1) # because it is one based
        p_queue = []
        heapq.heappush(p_queue,(0,1)) # 1 is the start node and
        #dist from sourcce(itself is 0) is 0
        parent[1] = 1
        distance[1] = 0
        sum = 0
        while len(p_queue) > 0 :
            dist,node = heapq.heappop(p_queue)
            if dist > distance[node]:
                continue
            distance[node] = dist
            for nei,weight in adj[node]:
                new_dist = dist + weight
                if new_dist >= distance[nei] :
                    continue
                parent[nei] = node
                distance[nei] = new_dist
                heapq.heappush(p_queue,(new_dist,nei))
        if distance[n] == float("inf"):
            return [-1]
        path = []
        node = n
        sum = distance[node]
        while parent[node] != node : #parent[1] = 1
            path.append(node)
            node = parent[node] # 5<- 3 somewhat reverse
        ans = []
        ans.append(sum)
        path.append(1)
        ans = ans + path[::-1]
        return ans
#[dist , path]