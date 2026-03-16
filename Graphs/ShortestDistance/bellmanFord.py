#User function Template for python3

class Solution:
    def bellmanFord(self, V, edges, src):
        #code here
        distance = [ 10**8 for _ in range(V)]
        distance[src] = 0
        for i in range(V - 1):
            for u,v,w in edges :
                if distance[u] != 10**8 and distance[u] + w  < distance[v]: #if a node is reachible only then check inf - somehting < inf
                    distance[v] = distance[u] + w

        for u,v,w in edges :
                if distance[u] != 10**8 and distance[u] + w  < distance[v]:
                    return [-1]
        
        return distance

# it is also used to get minimum distance from source to  all nodes
#it can also work for negative weights