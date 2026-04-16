#min insertion   to make a string palindrome
#LCS between string and its reverse will give us the longest palindromic subsequence
# n - len(LCS)
class Solution:
    def solve(self,i,j,s1,s2,dp):
        if i == -1 or j == -1:
            return 0
        if dp[i][j] != - 1 :
            return dp[i][j]
        if s1[i] == s2[j]:
            dp[i][j] =  1 + self.solve(i-1,j-1,s1,s2,dp)
            return dp[i][j]
        else :
            a = self.solve(i-1,j,s1,s2,dp)
            b = self.solve(i,j-1,s1,s2,dp)
            dp[i][j] = max(a,b)
            return dp[i][j]

    def minInsertions(self, s: str) -> int:
        s1 = s[::-1]
        n = len(s)
        dp = [ [-1 for _ in range(n)] for _ in range(n)]
        a = self.solve(n-1,n-1,s,s1,dp) 
        return n - a


# class Solution:
#     def minInsertions(self, s: str) -> int:
#         s1 = s[::-1]
#         n = len(s)
#         dp = [ [0 for _ in range(n+1)] for _ in range(n + 1)]
#         for i in range(1,n+1):
#             for j in range(1,n+1):
#                 if s[i-1] == s1[j-1]:
#                     dp[i][j] = 1 + dp[i-1][j-1]
#                 else :
#                     dp[i][j] = max(dp[i-1][j] , dp[i][j-1])  
#         return n - dp[n][n]




class Solution:
    def minInsertions(self, s: str) -> int:
        s1 = s[::-1]
        n = len(s)
        prev = [0 for _ in range(n+1)] 
        for i in range(1,n+1):
            curr = [0 for _ in range(n+1)]
            for j in range(1,n+1):
                if s[i-1] == s1[j-1]:
                    curr[j] = 1 + prev[j-1]
                else :
                    curr[j] = max(prev[j] , curr[j-1])  
            prev = curr
        return n - prev[n]