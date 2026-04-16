class Solution:

    def nthFibonacci(self, n: int) -> int:
        # code here
        if n <= 1 :
            return n
        prev2,prev = 0,1
        for i in range(2,n+1):
            curr = prev2 + prev
            prev2 = prev
            prev = curr
        return prev


# dp[i-1] = prev , dp[i] = curr 
# inner loop is prev
