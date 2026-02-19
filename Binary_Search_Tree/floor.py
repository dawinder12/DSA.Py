class Solution:
    ans = float("-inf")
    check = False
    def solve(self ,  root , x):
        if not root :
            return
        if root.data <= x :
            self.ans = max( self.ans , root.data)
            self.check = True
            self.solve(root.right , x)
        else :
            self.solve(root.left,x)
            
    def floor(self, root, x):
        # code here
        self.solve( root , x )
        if self.check == False:
            return -1
        return self.ans