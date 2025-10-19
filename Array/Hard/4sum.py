# def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#     n = len(nums)
#     if n < 4:
#         return []
    
#     my_set = set()  # stores unique quadruplets

#     # 👫 fix first two indices
#     for i in range(0, n):
#         for j in range(i + 1, n):
#             hash_set = set()  # tracks needed fourth numbers
#             # scan remaining indices for third element
#             for k in range(j + 1, n):
#                 fourth = target - (nums[i] + nums[j] + nums[k])

#                 if fourth in hash_set:           # found match
#                     temp = [nums[i], nums[j], nums[k], fourth]
#                     temp.sort()
#                     my_set.add(tuple(temp))

#                 # add current third element for future matches
#                 hash_set.add(nums[k])

#     # convert to required list format
#     result = [list(ans) for ans in my_set]
#     return result



def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    n = len(nums)
    ans = []
    nums.sort()  # Step 1: sort to simplify duplicates

    # 🚶‍♂️ Step 2: pick first two numbers
    for i in range(0, n):
        if i > 0 and nums[i] == nums[i - 1]:  # skip duplicates for i
            continue

        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:  # skip duplicates for j
                continue

            # Step 3: two-pointer search for remaining two
            k = j + 1               # left pointer
            l = n - 1               # right pointer

            while k < l:
                total = nums[i] + nums[j] + nums[k] + nums[l]

                if total == target:
                    ans.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1

                    # skip duplicate values for k
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    # skip duplicate values for l
                    while l > k and nums[l] == nums[l + 1]:
                        l -= 1

                elif total < target:
                    k += 1           # need a larger sum

                else:
                    l -= 1           # need a smaller sum

    return ans