class Solution:
    def solve(self,i,j,m,n,obstacleGrid,dp):
        if i == 0 and j == 0 :
            return 1
        elif i < 0 or j < 0 or obstacleGrid[i][j] == 1:
            return 0
        if dp[i][j] != - 1 :
            return dp[i][j]
        w1 = self.solve(i-1,j,m,n,obstacleGrid,dp)
        w2 = self.solve(i,j-1,m,n,obstacleGrid,dp)
        dp[i][j] = w1 + w2
        return dp[i][j]
        

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.solve(m-1,n-1,m,n,obstacleGrid,dp)


# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         m = len(obstacleGrid)
#         n = len(obstacleGrid[0])
#         if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
#             return 0
#         dp = [[-1 for _ in range(n)] for _ in range(m)]
#         dp[0][0] = 1
#         for i in range(m):
#             for j in range(n):
#                 if i == 0 and j == 0 :
#                     continue
#                 if obstacleGrid[i][j] == 1 :
#                     dp[i][j] = 0
#                     continue
#                 if i > 0 :
#                     down = dp[i-1][j]
#                 else :
#                     down = 0
#                 if j > 0 :
#                     right = dp[i][j-1]
#                 else :
#                     right = 0
#                 dp[i][j] = down + right
#         return dp[m-1][n-1]
