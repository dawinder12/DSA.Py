def rearrangeArray(nums):
        # n = len(nums)
        # result = []
        # pos = []
        # neg = []
        # for i in nums :
        #     if i > 0 :
        #         pos.append(i)
        #     else :
        #         neg.append(i)
        # for i in range(len(pos)):
        #     result.append(pos[i])
        #     result.append(neg[i])            
        # return result
        
    n = len(nums)
    pos,neg = 0 , 1
    result = [0]*n
    for i in range(n):
        if nums[i] > 0 :
            result[pos] = nums[i]
            pos += 2
        else :
            result[neg] = nums[i]
            neg += 2
    return result
    
    
    
    
print(rearrangeArray([1,2,3,-1,-2,-3]))

            
            

