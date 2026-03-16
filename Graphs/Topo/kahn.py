from collections import deque


class Solution:
    def topoSort(self, V, edges):
        adj_list = [[] for _ in range(V)]   # adjacency list
        indegrees = [0 for _ in range(V)]   # incoming edge counts

        # build graph and indegree array
        for u, v in edges:                  # edge u → v
            adj_list[u].append(v)
            indegrees[v] += 1

        queue = deque()                     # vertices ready to be processed
        result = []                         # final topological order

        # add all starting points (indegree == 0)
        for i in range(V):
            if indegrees[i] == 0:
                queue.append(i)

        # BFS over the DAG
        while queue:
            current_node = queue.popleft()
            result.append(current_node)

            # remove current_node’s edges
            for adjNode in adj_list[current_node]:
                indegrees[adjNode] -= 1
                if indegrees[adjNode] == 0:  # new node becomes ready
                    queue.append(adjNode)

        return result                       # contains V vertices in order