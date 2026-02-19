class Solution:
    ans = None
    def search(self,root , val):
        if root == None :
            return 
        if root.val == val :
            self.ans = root
            return
        if val > root.val and root.right:
            self.search(root.right , val)
        else :
            self.search(root.left , val)

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None :
            return None
        self.search( root , val)
        return self.ans