class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        ans = []
        result = {}
        line = 0
        queue.append( (root , line))
        while queue :
            e,line = queue.popleft()
            if not e :
                continue
            result[line] = e.val
            if e.left :
                queue.append( (e.left , line + 1))
            if e.right :
                queue.append( (e.right , line + 1))
        for k,v in sorted(result.items()):
            ans.append(result[k])
        return ans