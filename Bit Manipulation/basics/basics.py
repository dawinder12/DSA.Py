# # . Get ith bit

# 2. Set ith bit

# 3. Clear ith bit


def bitManipulation(num, i):
        # Code here
        i = i - 1 
        a = 1 << i 
        print("0",end = " ") if num  & a == 0 else print("1",end=' ')
        
        print(num |  a ,end = " ")
        
        b = ~a
        print( num & b )
        