class Solution:
    def solve(self , root , val  , temp):
        if root.val < val :
            if root.right == None :
                root.right = temp
                return
            self.solve(root.right ,val, temp)
        if root.val > val :
            if root.left == None :
                root.left = temp
                return
            self.solve(root.left ,val, temp)
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp = TreeNode(val)
        if not root :
            return temp
        self.solve(root , val , temp )
        return root
# always at leaf