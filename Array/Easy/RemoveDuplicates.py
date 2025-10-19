#Brute Force

# def removeDuplicates(nums: List[int]) -> int:
#     hash_map = {}
#     for i in nums :
#         hash_map[i] = hash_map.get(i,0) + 1
#     a = []
#     for key in hash_map:
#         a.append(key)
#     for _ in range(len(hash_map)):
#         nums[_] = a[_]
#     return len(hash_map)


#Optimal

def removeDuplicates(self, nums: List[int]) -> int:
    i,j = 0,1
    while j < len(nums):
       if nums[i] == nums[j]:
           j += 1
       else :
           i += 1
           nums[i],nums[j] = nums[j],nums[i]
           j += 1
    return i + 1


