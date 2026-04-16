# 0 was not here a[i] >= 1
class Solution:
    def minDifference(self, arr):
        # code here
        total = sum(arr)
        # S1 + S2 = Total
        n = len(arr)
        dp = [[False for _ in range(total + 1)] for _ in range(n)]
        for _ in range(n):
            dp[_][0] = True #if total is 0 -> True i.e Select NOne
        if arr[0] <= total :
            dp[0][arr[0]] = True #if total is arr[0] then it is TRue
        for i in range(1,n):
            for j in range(total + 1):
                if arr[i] > j :
                    pick = False
                else :
                    pick = dp[i-1][j-arr[i]]
                not_pick = dp[i-1][j]
                dp[i][j] = pick or not_pick
        ans = float("inf")
        for i in range(total + 1):
            if dp[n-1][i] :
                s1 = i
                s2 = total - s1
                temp = abs(s1-s2)
                ans = min(ans,temp)
        return ans