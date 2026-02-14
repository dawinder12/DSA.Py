class Solution:
    Check = True
    def ans(self,root):
        if root == None :
            return 0
        l_h = self.ans(root.left)
        r_h = self.ans(root.right)
        if abs(l_h - r_h) > 1 :
            self.Check = False
        return 1 + max(l_h , r_h)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None :
            return True
        self.ans(root)
        if self.Check == False :
            return False
        else :
            return True