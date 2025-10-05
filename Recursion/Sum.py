# Given an integer n, calculate the sum of series 13 + 23 + 33 + 43 + … till n-th term.

def sumOfSeries(n):
        #code here
        if n == 1 :
            return 1
        return n ** 3 + sumOfSeries(n - 1)