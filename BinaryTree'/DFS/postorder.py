# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def ans(self,root,order):
        if root == None :
            return 
        self.ans(root.left,order)
        self.ans(root.right,order)
        order.append(root.val)
        return order
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        return self.ans(root,[])
        