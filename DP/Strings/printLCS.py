#previous question is must to understand this code
def allLCS(self, s1, s2):
		# Code here
        n = len(s1)
        m = len(s2)
        text1 = s1
        text2 = s2
        dp = [ [0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else :
                    a = dp[i-1][j]
                    b = dp[i][j-1]
                    dp[i][j] = max(a,b)
        i,j = n,m
        result = []
        while i > 0 and j > 0 :
            if text1[i - 1] == text2[j-1]:
                result.append(text1[i-1])
                i -= 1
                j -= 1
            else :
                if dp[i-1][j] > dp[i][j-1]:
                     i -= 1
                else :
                    j -= 1
        return "".join(result[::-1])