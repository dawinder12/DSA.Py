class Solution:
    def ans(self,root,order):
        if root == None :
            return 
        order.append(root.val)
        self.ans(root.left,order)
        self.ans(root.right,order)
        return order
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None :
            return []
        return self.ans(root,[])