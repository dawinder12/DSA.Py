from collections import deque
class Solution:
    def solve(self , V,node,parent,adj,visited):
        visited[node] = 1
        for adjnode in adj[node]:
            if visited[adjnode] == 0 :
                if self.solve(V,adjnode,node,adj,visited):
                    return True
            else :
                if adjnode != parent :
                    return True
        return False
    def isCycle(self, V, edges):
		#Code here
	    adj = [[] for _ in range(V)]
	    for u,v in edges :
		    adj[v].append(u)
		    adj[u].append(v)
	    visited = [0] * (V) 
	    for i in range(V):
		    if visited[i] == 1 :
		        continue
		    if self.solve(V,i,-1,adj,visited) :
		        return True
	    return False
		