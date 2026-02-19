class Solution:
    ans = float("inf")
    check = False
    def solve(self , root , x) :
        if root == None :
            return
        if root.data >= x :
            self.check = True
            self.ans = min( self.ans , root.data)
            self.solve(root.left , x)
        if root.data < x :
            self.solve( root.right , x)
            
    def findCeil(self,root, x):
        # code here
        self.solve( root , x )
        if not self.check :
            return -1
        return self.ans