class Solution:
    def solve(self,i,j,grid,dp):
        if i == 0 and j == 0 :
            return grid[0][0]
        if i < 0 or j < 0 :
            return float("inf")
        if dp[i][j] != - 1 :
            return dp[i][j]
        up = grid[i][j] + self.solve(i-1,j,grid,dp)
        left = grid[i][j] + self.solve(i,j-1,grid,dp)
        dp[i][j] = min(up,left)
        return dp[i][j]
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.solve(m-1,n-1,grid,dp)



# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         m = len(grid)
#         n = len(grid[0])
#         dp = [[-1 for _ in range(n)] for _ in range(m)]
#         dp[0][0] = grid[0][0]
#         for i in range(m):
#             for j in range(n):
#                 if i == 0 and j == 0 :
#                     continue
#                 if i > 0 :
#                     down = grid[i][j] + dp[i-1][j]
#                 else :
#                     down = float("inf")
#                 if j > 0 :
#                     right = grid[i][j] + dp[i][j-1]
#                 else :
#                     right = float("inf")
#                 dp[i][j] = min(down,right)
#         return dp[m-1][n-1]




