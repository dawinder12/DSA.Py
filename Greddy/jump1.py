class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0 
        n = len(nums)
        maxi = 0
        while i < n :
            if i > maxi :
                return False
            maxi = max(maxi , i + nums[i])
            i += 1
        return True
            


        