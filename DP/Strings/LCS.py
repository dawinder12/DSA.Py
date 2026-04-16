class Solution:
    def solve(self,i,j,text1,text2,dp):
        if i == -1 or j == - 1 :
            return 0
        if dp[i][j] != - 1:
            return dp[i][j]
        if text1[i] == text2[j]:
            dp[i][j] =  1 + self.solve(i-1,j-1,text1,text2,dp)
            return dp[i][j]
        else :
            a = self.solve(i-1,j,text1,text2,dp)
            b = self.solve(i,j-1,text1,text2,dp)
            dp[i][j] =  0 + max(a,b)  
            return dp[i][j]      
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        return self.solve(n-1,m-1,text1,text2,dp)



class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        #just check condition for memoization i == -1 or j == -1 :
        # retunr 0 but in py[-1] is last so we add extra column in start and row
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1,n + 1):
            for j in range(1,m + 1):
                if text1[i - 1 ] == text2[j - 1]:
                    dp[i][j] =  1 + dp[i-1][j-1]
                else :
                    a = dp[i-1][j]
                    b = dp[i][j-1]
                    dp[i][j] =  0 + max(a,b)  
        return dp[n][m]