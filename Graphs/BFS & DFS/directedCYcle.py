from collections import deque
class Solution:
    def dfs(self,node,adj,visited,path):
        visited[node] = 1
        path[node] = 1
        for i in adj[node]:
            if visited[i] == 1 :
                if path[i] == 1: # it was already visited and was in my path
                    return True
            if self.dfs(i,adj,visited,path):
                return True
        path[node] = 0 # if its path are built now remove it work on other
        return False
    def isCyclic(self, V, edges):
        # code here
        adj = [[] for _ in range(V)]
        for u,v in edges :
            adj[u].append(v)
        visited = [0] * V
        path =  [0] * V
        for i in range(V):
            if visited[i] == 1 :
                continue
            if self.dfs(i,adj,visited,path):
                return True
        return False
            