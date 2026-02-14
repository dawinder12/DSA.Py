class Solution:
    def ans(self,root,order):
        if root == None :
            return 
        self.ans(root.left,order)
        order.append(root.val)
        self.ans(root.right,order)
        return order
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None :
            return []
        return self.ans(root,[])