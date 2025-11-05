
def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 :
            return nums[0]
        i = 0 
        j = n - 1
        minel = inf
        while i <= j :
            mid = ( i + j ) // 2
            if nums[mid] < nums[j]:
                minel = min(minel,nums[mid])
                j = mid - 1
            else :
                minel = min(minel,nums[i])
                i = mid + 1
        return minel



        