# def threeSum(nums):  # O(n^2)
#         idk = False
#         for i in nums :
#             if i != 0 :
#                 idk = True
#         if not idk :
#             return [[0,0,0]]
#         n = len(nums)
#         result = set()
#         for i in range(0,n-1):
#             my_set = set()
#             temp = []
#             for j in range(i+1,n):
#                 sum = nums[i] + nums[j]
#                 if -sum in my_set :
#                     idk = [nums[i],nums[j],-sum]
#                     idk.sort()
#                     result.add(tuple(idk))
#                 my_set.add(nums[j])
#         return [ list(ans)  for ans in result]


def threeSum(nums):
        ans = []
        n = len(nums)
        nums.sort()  # sort first for two-pointer technique

        for i in range(n):
            # skip duplicate fixed elements
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            # set up the two pointers
            j = i + 1
            k = n - 1

            # move pointers toward each other
            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]

                if total_sum < 0:
                    j += 1                     # need a larger sum
                elif total_sum > 0:
                    k -= 1                     # need a smaller sum
                else:
                    # found a valid triplet
                    temp = [nums[i], nums[j], nums[k]]
                    ans.append(temp)

                    # move both pointers and skip duplicates
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return ans