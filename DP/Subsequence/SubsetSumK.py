class Solution:
    def solve(self,i,arr,sum,curr,dp):
        if i == len(arr) :
            if curr == sum :
                return True
            return False
        if curr == sum :
            return True
        if curr > sum :
            return False
        if dp[i][curr] != -1 :
            return dp[i][curr]
        take = self.solve(i+1,arr,sum,curr + arr[i],dp)
        not_take =  self.solve(i+1,arr,sum,curr,dp)
        dp[i][curr] = take or not_take
        return dp[i][curr]
        
        
    def isSubsetSum (self, arr, sum):
        # code here 
        n = len(arr)
        dp = [[-1 for _ in range(sum+1)] for _ in range(n)]
        return self.solve(0,arr,sum,0,dp)




def isSubsetSum(self, arr, target):
        n = len(arr)
        
        dp = [[False for _ in range(target+1)] for _ in range(n)]
        
        # base case
        for i in range(n):
            dp[i][0] = True
        
        if arr[0] <= target:
            dp[0][arr[0]] = True # coz of only valid 1 length subset
            # think about meaning of dp[i][j]
        
        for i in range(1, n):
            for j in range(1, target+1):
                
                not_pick = dp[i-1][j]
                
                pick = False
                if j >= arr[i]:
                    pick = dp[i-1][j - arr[i]]
                
                dp[i][j] = pick or not_pick
        
        return dp[n-1][target]
        