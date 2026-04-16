class Solution:
    def solve(self,i,j,triangle,dp):
        if i == 0 and j == 0 :
            dp[i][j] = triangle[i][j]
            return dp[i][j]
        if i < 0 or j < 0 or j >= len(triangle[i]):
            dp[i][j] = float("inf")
            return dp[i][j]
        if dp[i][j] != - 1 :
            return dp[i][j]
        up = triangle[i][j] + self.solve(i-1,j,triangle,dp)
        dia = triangle[i][j] + self.solve(i-1,j-1,triangle,dp)
        dp[i][j] = min(up,dia)
        return dp[i][j]
        
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        n = len(triangle[-1])
        ans = float("inf")
        dp = [[-1 for i in range(n)] for i in range(m)]
        for i in range(n):
            ans = min(ans,self.solve(m-1,i,triangle,dp))
        return ans


# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         m = len(triangle)
#         n = len(triangle[-1])
#         ans = float("inf")
#         dp = [[-1 for i in range(n)] for i in range(m)]
#         dp[0][0] = triangle[0][0]
#         for i in range(m):
#             for j in range(n):
#                 if i == 0 and j == 0 :
#                     continue
#                 if i < 0 or  j < 0 or j >= len(triangle[i]):
#                     down = float("inf")
#                     dia = float("inf")
#                 else :
#                     down = triangle[i][j] + dp[i-1][j]
#                     dia = triangle[i][j] + dp[i-1][j-1]

#                 dp[i][j] = min(down,dia)
#         for i in range(n):
#             ans = min(ans,dp[m-1][i])
#         return ans

