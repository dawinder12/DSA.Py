class Solution:
    maxi = float("-inf")
    def solve(self,root,curr):
        if root == None :
            return 0 
        lh = self.solve(root.left , curr )
        rh = self.solve(root.right ,  curr)
        if lh < 0 : # -ve sum ko mt lo
            lh = 0
        if rh < 0:
            rh = 0
        self.maxi = max(self.maxi , root.val + lh + rh)
        return root.val + max(lh , rh ) # uper mai max sum hi bhejunga

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root and (root.left == None and root.right == None) :
            return root.val
        self.solve(root,0)
        return self.maxi