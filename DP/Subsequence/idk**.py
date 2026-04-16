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
            
    def countPartitions(self, arr, diff):
        # code here
        #s1 + s2 = total
        # S1 - S2 = d
        #total - s2 - s2 = d
        # (total - d )// 2 = s2
        # count numberr of subset with sum this
        total = sum(arr)
        target = ( total - diff ) // 2
        n = len(arr)
        if (total - diff) < 0 or (total - diff) % 2 != 0:
            return 0
        dp = [ [-1 for _ in range(target +1 )] for _ in range(n)]
        return self.solve(n-1,target,arr,dp)
    