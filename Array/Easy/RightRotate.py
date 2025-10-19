def rotate(nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # a = []
        # k = k % n
        # for _ in range(n) :
        #     a.append( nums[ ( _  -  k ) % n] ) 
        # nums[:] = a

        k = k % n
        nums[:] = nums[ n - k : ] + nums[ : n - k ]    
nums = [1,2,3,4,5] 
rotate(nums,k = 0)
print(nums)