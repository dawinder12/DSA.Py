class Solution:
    def solve(self,root,curr):
        if not root :
            return 0
        lh = self.solve(root.left,curr)
        rh = self.solve(root.right,curr)
        curr = lh + rh 
        self.maxi = max(self.maxi , curr)
        return 1 + max(lh,rh)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxi = 0
        self.solve(root,0)
        return self.maxi