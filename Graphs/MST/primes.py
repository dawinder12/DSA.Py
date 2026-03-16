import heapq
class Solution:
    def spanningTree(self, V, edges):
        # code here
        adj = [[] for _ in range(V)]
        for u,v,w in edges :
            adj[u].append((v,w))
            adj[v].append((u,w))
        p_queue = []
        p_queue.append((0,0)) # dist,node
        ans = 0
        visited = [-1] * V
        while len(p_queue) > 0 : # -> E
            dist,node = heapq.heappop(p_queue) #logE
            if visited[node] == 1 :
                continue
            ans +=  dist
            visited[node] = 1
            for nei ,w in adj[node]: # -> E
                if visited[nei] == 1 :
                    continue
                heapq.heappush(p_queue,(w,nei))#logE
        return ans



#tc - > ElogE