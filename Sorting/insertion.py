# def insertionSort( arr):
#         for i in range(1,len(arr)):
#             key = arr[i]
#             j = i - 1
#             while j >= 0 and arr[j] >= key:
#                 arr[j + 1] = arr[j]
#                 j -= 1
#             arr[j + 1] = key
#         return arr
    
    
    
#Decreasing order 
def insertionSort( arr):
        for i in range(1,len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] <= key: # change sign 
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
print(insertionSort([5,2,8,2,1,-1,0,69,3,2]))