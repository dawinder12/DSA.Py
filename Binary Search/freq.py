
def countFreq(self, arr, target):
        # code here
        left = -1
        n = len(arr)
        i = 0
        j = n - 1
        while i <= j:
            mid = ( i + j ) // 2
            if arr[mid] == target :
                left = mid
                j = mid - 1
            elif arr[mid] > target :
                j = mid - 1
            else :
                i = mid + 1
        if left == -1 :
            return 0
        right = 0
        i = 0 
        j = n - 1
        while i <= j :
            mid = ( i + j ) // 2
            if arr[mid] == target :
                right = mid 
                i = mid + 1
            if arr[mid]  > target :
                j = mid - 1
            else :
                i = mid + 1 
        return right - left  + 1