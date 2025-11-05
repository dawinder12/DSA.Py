def search(self, nums: List[int], target: int) -> int:
        n         = len(nums)
        low, high = 0, n - 1
        
        while low <= high:
            mid = (low + high) // 2          # middle index
            
            if nums[mid] == target:          # target found
                return mid
            
            # ----- identify the sorted half -----
            if nums[low] <= nums[mid]:       # left half is sorted
                # target lies within the left half?
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1           # search left half
                else:
                    low  = mid + 1           # search right half
            else:                            # right half is sorted
                # target lies within the right half?
                if nums[mid] <= target <= nums[high]:
                    low  = mid + 1           # search right half
                else:
                    high = mid - 1           # search left half
        
        return -1                            # target not found