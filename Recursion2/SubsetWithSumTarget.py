from typing import List

def backtrack(subset: List[int], index: int, total: int):
    # Base case: If sum equals K, add a copy of the subset to result
    if total == k:
        result.append(subset.copy())
        return
    # Prune: If sum exceeds K, stop this path
    elif total > k:
        return
    # Base case: If index is out of bounds, stop
    if index >= len(nums):
        return
    
    # Choice 1: Include the current element
    subset.append(nums[index])  # Add to subset
    Sum = total + nums[index]   # Update sum
    backtrack(subset, index + 1, Sum)  # Recurse to next index
    
    # Backtrack: Undo the inclusion
    subset.pop()                # Remove last element
    Sum = total                 # Reset sum
    
    # Choice 2: Exclude the current element
    backtrack(subset, index + 1, Sum)  # Recurse without adding

result = []                     # List to store all valid subsequences
nums = [1, 2, 3, 4, 3, 2, 1, 1, 1, 1]  # Example array
k = 3                           # Target sum
backtrack([], 0, 0)             # Start backtracking
print(result)                   # Print the result