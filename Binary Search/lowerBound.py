# Given a sorted array arr[] and an integer x, find the index (0-based) of the largest element 
# in arr[] that is less than or equal to x. This element is called the floor of x. 
# If such an element does not exist, return -1.

# Note: In case of multiple occurrences of ceil of x, return the index of the last occurrence.



def findFloor(self, arr, x):
        # code here
        ans = -1
        i = 0
        j = len(arr) - 1
        while i <= j :
            mid = ( i + j ) // 2
            if arr[mid] >= x :
                ans = mid
                j = mid - 1
            else :
                i = mid + 1
        return ans
        