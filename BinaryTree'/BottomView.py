class Solution:
    def bottomView(self, root):
        # code here
        ans = []
        queue = deque()
        line = 0
        queue.append( (root , line) )
        result = {}
        while queue :
            e,line = queue.popleft()
            result[line] = e.data
            if e.left :
                queue.append( (e.left , line - 1))
            if e.right :
                queue.append( (e.right , line + 1))
        for k,v in sorted(result.items()):
            ans.append(result[k])
        return ans