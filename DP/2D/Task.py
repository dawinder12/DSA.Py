class Solution:
    def solve(self,mat,day,last,dp):
        if day == 0 :
            maxi = 0
            for i in range(3):
                if i != last :
                    maxi = max(maxi , mat[day][i])
            return maxi
        if dp[day][last] != - 1 :
            return dp[day][last]
        maxi = 0
        for i in range(3):
            if i != last :
                maxi = max(maxi , mat[day][i] + self.solve(mat,day-1,i,dp))
        dp[day][last] = maxi
        return  dp[day][last]
    def maximumPoints(self, mat):
        # code here
        n = len(mat)
        dp = [ [-1,-1,-1,-1] for _ in range(n)]
        return self.solve(mat,n-1,3,dp)


# class Solution:
#     def maximumPoints(self, mat):
#         # code here
#         n = len(mat)
#         dp = [ [-1,-1,-1,-1] for _ in range(n)]
#         dp[0][0] = max(mat[0][1],mat[0][2]) # t0 was taken previous
#         dp[0][1] = max(mat[0][2],mat[0][0])
#         dp[0][2] = max(mat[0][1],mat[0][0])
#         dp[0][3] = max(mat[0])
#         for day in range(1,n):
#             for last in range(0,4):
#                 maxi = 0
#                 for i in range(0,3):
#                     if i != last :
#                         maxi = max(maxi , mat[day][i] + dp[day-1][i])
#                 dp[day][last] = maxi
#         return dp[n-1][3]


                        