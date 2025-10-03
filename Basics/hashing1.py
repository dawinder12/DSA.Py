# Given an array arr of positive integers 
# and an integer x. Return the frequency of x in the array.

arr = [1, 1, 1, 1, 1]
x = 1

def findFrequency(arr, x):
        freq_dict = {}
        for num in arr :
            freq_dict[num] = freq_dict.get(num,0) + 1
        return  freq_dict.get(x,0)


print(findFrequency(arr,x))