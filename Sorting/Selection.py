#  Increasing Order
# def selectionSort(arr):
#         for i in range(len(arr)):
#             minIdx = i
#             for j in range(i + 1 , len(arr)):
#                 if arr[j] <= arr[minIdx]:
#                     minIdx = j
#             arr[i],arr[minIdx] = arr[minIdx],arr[i]
#         return arr



#Decreasing Order : 
def selectionSort(arr):
        for i in range(len(arr)):
            maxIdx = i
            for j in range(i + 1 , len(arr)):
                if arr[j] >= arr[maxIdx]:
                    maxIdx = j
            arr[i],arr[maxIdx] = arr[maxIdx],arr[i]
        return arr
    
print(selectionSort([5,2,8,2,1,-1,0,69,3,2]))