# Given an array arr, you need to reverse a subarray of that array. 
# The range of this subarray is given by indices l and r (1-based indexing).


def sol(arr,l,r):
        if l >= r :
            return 
        arr[l],arr[r]  = arr[r],arr[l]
        sol(arr,l + 1 , r - 1)
def reverseSubArray(arr,l,r):
    sol(arr,l,r)
    return arr
 
print(reverseSubArray([1, 2, 3 ,4 ,5, 6, 7],1,3))
	    
     
     
     
     
     
     