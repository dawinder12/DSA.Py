class Solution:
    def solve(self,i,j,matrix,dp):
        if i < 0 or j < 0 or j >= len(matrix[0]) :
            return float("inf")
        if i == 0 :
            return matrix[i][j]
        if dp[i][j] != float("inf") :
            return dp[i][j]
        up = matrix[i][j] + self.solve(i-1,j,matrix,dp)
        left_dia = matrix[i][j] + self.solve(i-1,j-1,matrix,dp)
        right_dia = matrix[i][j] + self.solve(i-1,j+1,matrix,dp)
        dp[i][j] = min(up,left_dia,right_dia)
        return dp[i][j]

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        cols = len(matrix[0])
        ans = float("inf")
        dp = [[float("inf") for _ in range(cols) ] for _ in range(row)]
        for i in range(cols):
            ans = min(ans,self.solve(row-1,i,matrix,dp))
        return ans


# class Solution:
#     def minFallingPathSum(self, matrix: List[List[int]]) -> int:
#         row = len(matrix)
#         cols = len(matrix[0])
#         dp = [[float("inf") for _ in range(cols) ] for _ in range(row)]
#         for i in range(cols):
#             dp[0][i] = matrix[0][i]
#         for i in range(1,row):
#             for j in range(cols):
#                 down = matrix[i][j] + dp[i-1][j]
#                 if j == cols - 1 :
#                     right = float("inf")
#                 else :
#                     right = matrix[i][j] + dp[i-1][j+1]
#                 if j == 0 :
#                     left = float("inf")
#                 else :
#                     left = matrix[i][j] + dp[i-1][j-1]
#                 dp[i][j] = min(down,left,right)
#         ans = float("inf")
#         for i in range(cols):
#             ans = min(ans,dp[row-1][i])
#         return ans

