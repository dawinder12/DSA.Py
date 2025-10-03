a = [1,4,6,7,88,33,5,1,1,6,7,3,3,5,5,77,88,98]
freq_dict = {}
n = len(a)
for _ in range(n):   # O(n)
    if a[_] in freq_dict: # O(1)
        freq_dict[a[_]] += 1 # O(1)
    else :
         freq_dict[a[_]] = 1 # O(1)
print(freq_dict)

hash_map = {}
for _ in range(len(a)):
    hash_map[a[_]] = hash_map.get(a[_],0) + 1 # .get => return value of key hash_map[a[_]] if exist or 0 if not
print(hash_map)