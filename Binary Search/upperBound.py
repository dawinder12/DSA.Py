# Problem statement
# You are given a sorted array ‘arr’ containing ‘n’ integers and an integer ‘x’.
# Implement the ‘upper bound’ function to find the index of the upper bound of 'x' in the array.



# Note:
# 1. The upper bound in a sorted array is the index of the first value that is greater than a given value. 
# 2. If the greater value does not exist then the answer is 'n', Where 'n' is the size of the array.
# 3. Try to write a solution that runs in log(n) time complexity.

def upperBound(arr: [int], x: int, n: int) -> int:
    # Write your code here.
    ans = len(arr)
    i = 0
    j = ans - 1
    while i <= j :
        mid = (i + j) // 2
        if arr[mid] > x :
            ans = mid 
            j = mid - 1
        else :
            i = mid + 1
    return ans 

