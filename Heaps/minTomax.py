def max_heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)


def convert_min_to_max_heap(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        max_heapify(arr, n, i)

    return arr

# just treat this min arr as normal arr