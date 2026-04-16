#User function Template for python3
class Solution:
    def solve(self,i,target,arr,dp):
        if i == -1 :
            if target == 0 :
                return 1
            return 0
        if dp[i][target] != - 1 :
            return dp[i][target]
        if arr[i] > target :
            pick = 0
        else :
            pick = self.solve(i-1,target-arr[i],arr,dp)
        not_pick = self.solve(i-1,target,arr,dp)
        dp[i][target] = pick + not_pick
        return dp[i][target] 
    def perfectSum(self, arr, target):
        # code here
        n = len(arr)
        dp =  [ [-1 for _ in range(target + 1)]  for _ in range(n)]
        return self.solve(n-1,target,arr,dp)


