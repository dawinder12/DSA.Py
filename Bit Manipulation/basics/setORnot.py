def checkKthBit( n, k):
        # code here
        a = 1 << k 
        return n & a