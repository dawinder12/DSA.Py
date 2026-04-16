class Solution:
    def minCost(self, height):
        # code here
        n = len(height)
        if n == 1 :
            return 0
        dp = [-1] * (n)
        dp[0] = 0
        dp[1] = abs(height[0] - height[1])
        for i in range(2,n):
            a = dp[i-1] + abs(height[i] - height[i-1])
            b = dp[i-2] + abs(height[i] - height[i-2])
            dp[i] = min(a,b)
        return dp[n-1]

# class Solution:
#     def func(self, height, index, dp):
#         if index == 0:
#             return 0
#         if dp[index] != -1:
#             return dp[index]
#         jump1 = self.func(height, index - 1, dp) + abs(
#             height[index] - height[index - 1]
#         )
#         if index > 1:
#             jump2 = self.func(height, index - 2, dp) + abs(
#                 height[index] - height[index - 2]
#             )
#         else:
#             jump2 = float("inf")
#         dp[index] = min(jump1, jump2)
#         return dp[index]

#     def minCost(self, height):
#         n = len(height)
#         dp = [-1] * n
#         return self.func(height, n - 1, dp)



# class Solution:
#     def minCost(self, height):
#         n = len(height)
#         prev2 = 0
#         prev = 0
#         for index in range(1, n):
#             jump1 = prev + abs(height[index] - height[index - 1])
#             if index > 1:
#                 jump2 = prev2 + abs(height[index] - height[index - 2])
#             else:
#                 jump2 = float("inf")
#             curr = min(jump1, jump2)
#             prev2 = prev
#             prev = curr
#         return prev