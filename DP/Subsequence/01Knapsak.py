class Solution:
    def solve(self,i,w,val,wt,dp):
        if i == 0 :
            if wt[i] <= w :
                return val[i]
            else :
                return 0
        if dp[i][w] != - 1 :
            return dp[i][w]
        if wt[i] > w :
            pick = 0
        else :
            pick = val[i] + self.solve(i-1,w-wt[i],val,wt,dp)
        not_pick = self.solve(i-1,w,val,wt,dp)
        dp[i][w] = max(pick,not_pick)
        return dp[i][w]
        
    def knapsack(self, W, val, wt):
        # code here
        n = len(val)
        dp = [ [-1 for _ in range(W + 1)] for _ in range(n)] 
        return self.solve(n-1,W,val,wt,dp)



# def knapsack(self, W, val, wt):
#         # code here
#         n = len(val)
#         dp = [ [0 for _ in range(W + 1)] for _ in range(n)] 
#         for i in range(n):
#             dp[i][0] = 0 
#         for i in range(W + 1):
#             if wt[0] <= i:
#                 dp[0][i] = val[0]
#         for i in range(1,n):
#             for j in range(W + 1):
#                 if wt[i] > j :
#                     pick = 0
#                 else :
#                     pick = val[i] + dp[i-1][j-wt[i]]
#                 not_pick = 0 + dp[i-1][j]
#                 dp[i][j] = max(pick,not_pick)
#         return dp[n-1][W]
        

