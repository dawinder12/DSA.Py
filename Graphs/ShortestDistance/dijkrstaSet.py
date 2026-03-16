import sys

class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # ------- 1. Build adjacency list -------
        adj_list = [[] for _ in range(V)]
        for u, v, d in edges:
            adj_list[u].append([v, d])

        # ------- 2. Distance array & set -------
        distance = [sys.maxsize for _ in range(V)]
        distance[src] = 0

        my_set = set()
        my_set.add((0, src))                       # (dist, node)

        # ------- 3. Main loop -------
        while len(my_set) != 0:
            dist, node = min(my_set)               # slow O(k) min()
            my_set.discard((dist, node))           # remove picked pair

            for adjNode, weight in adj_list[node]:
                dist_trav = dist + weight          # path through 'node'
                if dist_trav < distance[adjNode]:  # found a better path
                    if distance[adjNode] != sys.maxsize:
                        my_set.discard((distance[adjNode], adjNode))
                    distance[adjNode] = dist_trav
                    my_set.add((dist_trav, adjNode))

        return distance