class Solution:
    def solve(self,i,buy,prices,dp):
        if i == len(prices):
            return 0
        if dp[i][buy] != - 1 :
            return dp[i][buy]
        if buy == 1 :
            pick = -prices[i] + self.solve(i+1,0,prices,dp) # if it is picked/bought profit is less
            not_buy = 0 + self.solve(i+1,1,prices,dp)
            dp[i][buy] =  max(pick,not_buy)
            return dp[i][buy]
        else :
            sell = prices[i] + self.solve(i+1,1,prices,dp)#sell - > profit + 
            not_sell = 0 + self.solve(i+1,0,prices,dp)
            dp[i][buy] =  max(sell,not_sell)
            return dp[i][buy]
    def maxProfit(self, prices: List[int]) -> int:
        dp =  [ [-1 for _ in range(2)] for _ in range(len(prices))]
        return self.solve(0,1,prices,dp) # (idx,buy,prices)
        #buy == 1 -> you can buy and skip as well
        #buy == 0 -> you cannt buy it -> sell or skip it
    



# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         n = len(prices)
#         dp =  [ [0 for _ in range(2)] for _ in range(n + 1)]
#         dp[n][0] = 0
#         dp[n][1] = 0
#         for i in range(n-1,-1,-1):
#             for buy in range(2):
#                 if buy == 1 :
#                     pick = -prices[i] + dp[i+1][0]
#                     not_buy = 0 + dp[i+1][1]
#                     dp[i][buy] = max(pick,not_buy)
#                 else :
#                     sell = prices[i] + dp[i+1][1]
#                     not_sell = 0 + dp[i+1][0]
#                     dp[i][buy] = max(sell,not_sell)
#         return dp[0][1]


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         n = len(prices)
#         prev =   [0 for _ in range(2)] 
#         for i in range(n-1,-1,-1):
#             curr = [0 for _ in range(2)]
#             for buy in range(2):
#                 if buy == 1 :
#                     pick = -prices[i] + prev[0]
#                     not_buy = 0 + prev[1]
#                     curr[buy] = max(pick,not_buy)
#                 else :
#                     sell = prices[i] + prev[1]
#                     not_sell = 0 + prev[0]
#                     curr[buy] = max(sell,not_sell)
#             prev = curr
#         return prev[1]