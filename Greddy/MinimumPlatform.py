class Solution:    
    def minPlatform(self, arr, dep):
        # code here
        trains = []
        n = len(arr)
        if n == 1 :
            return 1
        arr.sort()
        dep.sort()
        count = 1
        platform = 1 
        i,j = 1,0
        while i < n and j < n :
            if arr[i] <= dep[j]:
                count += 1
                i += 1
            else :
                count -= 1
                j += 1
            platform = max(platform , count)
        return platform
    
 # make a timeline
            
            