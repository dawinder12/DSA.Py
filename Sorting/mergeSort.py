def mergeSort(arr):
    if len(arr) <= 1 :
        return arr
    mid = (len(arr)) // 2
    left_arr = arr[ : mid]
    right_arr = arr[ mid : ]
    left = mergeSort(left_arr)
    right = mergeSort(right_arr)
    return merge(left,right)

def merge(left,right):
    result = []
    i,j = 0,0
    n,m = len(left),len(right)
    while i < n  and  j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else :
            result.append(right[j])
            j += 1
    while i < n:
        result.append(left[i])
        i += 1
    while j < m :
        result.append(right[j])
        j += 1
    return result
print(mergeSort([4,1,3,9,7]))
            