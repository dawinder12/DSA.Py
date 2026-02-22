def build_min_heap(arr):
    n = len(arr)

    # Start from last non-leaf node
    for i in range(n//2 - 1, -1, -1):
        min_heapify(arr, n, i)

    return arr

# tc = O(n) not nlogn