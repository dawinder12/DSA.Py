# You are given an array arr[] containing positive integers. 
# The elements in the array arr[]
# range from  1 to n (where n is the size of the array), 
# and some numbers may be repeated or absent.
# Your have to count the frequency of all numbers in the range 1 to n
# and return an array of size n such that result[i] 
# represents the frequency of the number i (1-based indexing).



arr = [2, 3, 2, 3, 5]

def frequencyCount( arr):
        hash_map = [0] * (len(arr))
        for num in arr :
            hash_map[num - 1] += 1
        return hash_map
print(frequencyCount(arr))