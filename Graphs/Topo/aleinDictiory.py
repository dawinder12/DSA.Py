class Solution:
    def check(self,node,visited,adj):
        visited[node] = 1
        
        for nei in adj[node]:
            if visited[nei] == 1:
                return True
            
            if visited[nei] == 0 and self.check(nei,visited,adj):
                return True
        
        visited[node] = 2
        self.stack.append(node)
        return False


    def findOrder(self, words):
        self.stack = []
        
        adj = [[] for _ in range(26)]
        present = set()

        for w in words:
            for c in w:
                present.add(ord(c)-97)

        for i in range(1,len(words)):
            a = words[i-1]
            b = words[i]

            limit = min(len(a),len(b))
            if len(a) > len(b) and a[:limit] == b[:limit]:
                return ""
            for j in range(limit):
                if a[j] != b[j]:
                    u = ord(a[j]) - 97
                    v = ord(b[j]) - 97
                    adj[u].append(v)
                    break
        
        visited = [0] * 26
        
        for i in present:
            if visited[i] == 0:
                if self.check(i,visited,adj):
                    return ""
        
        ans = []
        for i in self.stack[::-1]:
            ans.append(chr(i + 97))
        
        return "".join(ans)