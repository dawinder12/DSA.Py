class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None :
            return 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return 1 + max(left_height , right_height) # khud ka height  + max ..