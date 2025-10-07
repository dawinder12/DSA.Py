def bubbleSort(arr):
        # code here
        n = len(arr)  - 2
        isSwapped = False
        for i in range(n,0 - 1,-1):
            for j in range(i+1):
                if arr[j] >= arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
                    isSwapped = True
            if isSwapped == False:
                return arr
        return arr
            
print(bubbleSort([5,2,8,2,1,-1,0,69,3,2]))