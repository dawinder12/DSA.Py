from collections import deque
class Solution:
    def dfs(self,node,adj,visited):
        visited[node] = 1
        for nei in adj[node]:
            if visited[nei] == 1 :
                continue
            self.dfs(nei,adj,visited)
        self.stack.append(node)
    def topoSort(self, V, edges):
        # Code here
        self.stack = deque()
        adj = [[] for _ in range(V)]
        for u,v in edges :
            adj[u].append(v)
        visited = [0] * V
        for i in range(V):
            if visited[i] == 1 :
                continue
            self.dfs(i,adj,visited)
        ans = []
        while len(self.stack)>0:
            ans.append(self.stack.pop())
        return ans