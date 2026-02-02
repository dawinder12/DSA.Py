class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return k
        ans,zeroes = 0,0
        l,r = 0,0
        while r < len(nums):
            if nums[r] == 0 : #check invalid window and make it valid and size of window = ans
                zeroes += 1   # window never shrinks
            if zeroes > k :
                if nums[l] == 0 :
                    zeroes -= 1
                l += 1
            ans = max(ans , r - l + 1)
            r += 1 
        return ans
