class Solution:
    def solve(self,i,buy,limit,prices,dp):
        if i == len(prices) or limit == 0:
            return 0
        if dp[i][buy][limit] != -1 :
            return dp[i][buy][limit]
        if buy == 1 :
            pick = -prices[i] + self.solve(i+1,0,limit,prices,dp)
            not_buy = 0 + self.solve(i+1,1,limit,prices,dp)
            dp[i][buy][limit] = max(pick , not_buy)
        else :
            sell = prices[i] + self.solve(i+1,1,limit - 1,prices,dp)
            not_sell = 0 + self.solve(i+1,0,limit,prices,dp)
            dp[i][buy][limit] = max(sell,not_sell)
        return dp[i][buy][limit]
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp =  [ [ [-1 for _ in range(3)] for _ in range(3)] for _ in range(n) ] 
        return self.solve(0,1,2,prices,dp)