class Solution:
    def longCommSubstr(self, s1, s2):
        # code here
        n = len(s1)
        m = len(s2)
        dp = [ [0 for _ in range(m+1)] for _ in range(n+1)] 
        maxi = 0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else :
                    dp[i][j] = 0
                maxi = max(maxi,dp[i][j])
        return maxi
        


class Solution:
    def solve(self, i, j, s1, s2, dp):
        if i == 0 or j == 0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if s1[i-1] == s2[j-1]:
            dp[i][j] = 1 + self.solve(i-1, j-1, s1, s2, dp)
            self.maxi = max(self.maxi, dp[i][j])
        else:
            dp[i][j] = 0
            
        self.solve(i-1, j, s1, s2, dp)
        self.solve(i, j-1, s1, s2, dp)

        return dp[i][j]

    def longCommSubstr(self, s1, s2):
        n, m = len(s1), len(s2)
        dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
        self.maxi = 0

        self.solve(n, m, s1, s2, dp)

        return self.maxi