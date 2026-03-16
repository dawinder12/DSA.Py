class Solution:
    def dfs_algo(self, node, adj, visited, result):
        # 1. Visit this node
        result.append(node)
        visited[node] = 1

        # 2. Recurse on each unvisited neighbor
        for neighbor in adj[node]:
            if not visited[neighbor]:
                self.dfs_algo(neighbor, adj, visited, result)

    def dfs(self, adj):
        total_nodes = len(adj)
        visited = [0] * total_nodes  # 0 = unvisited, 1 = visited
        result = []

        # Start DFS from node 0
        self.dfs_algo(0, adj, visited, result)
        return result