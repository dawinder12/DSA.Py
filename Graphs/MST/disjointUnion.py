class Disjoin:

    def __init__(self, n):
        # parent[i] = parent of node i
        # initially every node is its own parent
        # so each node is its own set
        self.parent = [i for i in range(n + 1)]   # 1-based indexing
        
        # size[i] = number of elements in the set whose root is i
        self.size = [1] * (n + 1)


    def find(self, x):
        # find the ultimate parent (root) of x

        # if x is its own parent → it is the root
        if self.parent[x] == x:
            return x
        
        # path compression:
        # make every node on the path point directly to the root
        # this reduces time complexity for future queries
        self.parent[x] = self.find(self.parent[x])

        return self.parent[x]


    def union(self, x, y):

        # find ultimate parents of both nodes
        px = self.find(x)
        py = self.find(y)

        # if both nodes already belong to same set
        # no need to union
        if px == py:
            return

        # size of both sets
        sx = self.size[px]
        sy = self.size[py]

        # union by size
        # attach smaller tree under bigger tree

        if sx > sy:
            # attach root of y under root of x
            self.parent[py] = px

            # update size of new root
            self.size[px] += sy

        elif sx < sy:
            # attach root of x under root of y
            self.parent[px] = py
            self.size[py] += sx

        else:
            # if sizes equal, attach any one
            self.parent[py] = px
            self.size[px] += sy