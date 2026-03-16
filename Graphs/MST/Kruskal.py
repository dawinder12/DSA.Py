class DisjointSet:
    def __init__(self,n):
        self.parent = [ i for i in range(n)]
        self.size = [1] * n
    
    def find(self,x):
        if self.parent[x] == x :
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv : # both the nodes are connected no need to make new edge
            return False
        if self.size[pu] > self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else :
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        return True

class Solution:
    def spanningTree(self, V, edges):
        # code here
        edges = sorted(edges,key = lambda x : x[2])
        distjoint = DisjointSet(V)
        ans = 0
        for u,v,w in edges :
            if distjoint.union(u,v):
                ans += w
        return ans
