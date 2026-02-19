class Solution:
    mini = 0
    def check(self ,  root ):
        if root.left == None :
            self.mini = root.data
            return
        self.check(root.left)
    def minValue(self, root):
        self.check(root)
        return self.mini