class Solution:
    def solve(self,i,j,m,n,dp):
        if i == m - 1 and j == n - 1 :
            return 1
        elif i >= m  or  j >= n :
            return 0
        if dp[i][j] != - 1 :
            return dp[i][j]
        w1 = self.solve(i+1,j,m,n,dp)
        w2 = self.solve(i,j+1,m,n,dp)
        dp[i][j] = w1 + w2
        return dp[i][j]
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [ [-1 for _ in range(n)] for _ in range(m)]
        return self.solve(0,0,m,n,dp)




# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp = [ [-1 for _ in range(n)] for _ in range(m)]
#         dp[0][0] = 1
#         for r in range(m):
#             for c in range(n):
#                 if r == 0 and c == 0 :
#                     continue
#                 if r > 0 :
#                     down = dp[r-1][c]
#                 else :
#                     down = 0
#                 if c > 0 :
#                     right = dp[r][c-1]
#                 else :
#                     right = 0
#                 dp[r][c] = down + right

#         return dp[m-1][n-1]






# __import__("atexit").register(lambda: open("display_runtime.txt","w").write("0"))