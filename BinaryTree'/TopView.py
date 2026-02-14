class Solution:
    def topView(self, root):
        # code here
        ans = []
        line = 0
        result = {}
        queue = deque()
        queue.append((root , line))
        while queue :
            e,line = queue.popleft()
            if line not in result :
                result[line] = e.data
            if e.left :
                queue.append((e.left , line - 1))
            if e.right :
                queue.append( (e.right , line + 1))
        
        for k,v in sorted(result.items()):
            ans.append(result[k])
        return ans
    
# Line Method first node of a line is the required node
# therefore check if that line number is present or not 