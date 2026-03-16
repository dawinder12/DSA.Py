class DisjointSet :
    def __init__(self,n):
        self.parent = [ i for i in range(V)]
        self.size = [1] * V

    def find(self,x):
        if self.parent[x] == x :
            return x 
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        
        if pu == pv :
            return True
        if self.size[pu] > self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else :
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
class Solution:
    def numProvinces(self, adj, V):
        # code here 
        dsu = DisjointSet(V)
        rows = len(adj)
        cols = len(adj[0])
        for r in range(rows):
            for c in range(cols):
                if adj[r][c] == 1 and r != c :
                    dsu.union(r,c)
        count = 0
        for i in range(V):
            if dsu.find(i) == i : # number of node who has ultimate parent as itself
                count += 1
        return count