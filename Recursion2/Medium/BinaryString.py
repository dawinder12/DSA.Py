# Given an integer n. You need to generate all the binary strings of n characters representing bits.

# Note: Return the strings in  ascending order.
def solve(self,idx,n,subset,result):
        if idx == n :
            result.append("".join(subset.copy()))
            return
        subset.append("1")
        self.solve(idx + 1 , n , subset , result)
        subset.pop()
        subset.append("0")
        self.solve(idx + 1 , n ,subset,result)
        subset.pop()
def binstr(self, n):
        # code here
        result = []
        self.solve(0,n,[],result)
        result.sort()
        return result