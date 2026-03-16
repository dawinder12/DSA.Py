from collections import deque
class Solution:
	def isCycle(self, V, edges):
		#Code here
		adj = [[] for _ in range(V)]
		for u,v in edges :
		    adj[v].append(u)
		    adj[u].append(v)
		visited = [0] * (V) 
		for j in range(V):  # becuase graph can be dissconnected
		    if visited[j] == 1 :
		        continue
		    queue = deque()
		    start_node = 0
		    visited[j] = 1
		    queue.append((j , -1)) # (node,parent)
		
		    while len(queue) > 0 :
		        node,parent = queue.popleft()
		    
		        for i in adj[node]:
		            if visited[i] == 0 :
		                visited[i] = 1
		                queue.append((i,node))
		            else :
		                if i == parent or i == start_node : # this node was visited and it was parent
		                  continue
		                else :
		                    return True # this node is visited but it was not parent i.e cycle
		return False
		
		
		
		
		