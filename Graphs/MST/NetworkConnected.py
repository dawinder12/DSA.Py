# remove and edge and reuse it to make the graph connected
class DisjointUnion:
    def __init__(self,n):
        self.parent = [ i  for i in range(n)]
        self.size = [1] * n
    
    def find(self,x):
        if self.parent[x] == x :
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv :
            return False
        if self.size[pu] > self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else :
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        return True
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        extra_edges = 0
        required_edge = -1 # component - 1 
        dsu = DisjointUnion(n)
        for u,v in connections :
            if not dsu.union(u,v) : #both are already connected by ultimate parent
                extra_edges += 1
        for i in range(n) :
            if dsu.find(i) == i : 
                required_edge += 1
        # for u,v in connections :
        #     if dsu.find(u) == dsu.find(v):
        #         extra_edges+= 1
        if extra_edges >= required_edge :
            return required_edge
        return -1
