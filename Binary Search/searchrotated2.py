
def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2              # Find the middle index

            if nums[mid] == target:              # If middle element is target, return True
                return True

            # If we encounter duplicates making it unclear which side is sorted
            if nums[low] == nums[mid] == nums[high]:
                high -= 1
                low += 1
                continue

            # Check if left half is sorted
            if nums[low] <= nums[mid]:
                # Target lies in the left half
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1               # Move to the left half
                else:
                    low = mid + 1                # Move to the right half
            # Else, right half is sorted
            else:
                # Target lies in the right half
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1                # Move to the right half
                else:
                    high = mid - 1               # Move to the left half

        return False                             # Target not found