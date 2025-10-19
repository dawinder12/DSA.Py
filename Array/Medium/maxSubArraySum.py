def check(arr):
        for i in arr : 
            if i > 0 :
                return False
        return True
def maxSubArray(nums):
        if check(nums):
            return max(nums)
        max_sum = 0
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum < 0 :
                sum = 0
            max_sum = max(max_sum,sum)
        return max_sum
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


        