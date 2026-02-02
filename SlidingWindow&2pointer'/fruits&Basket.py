class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r = 0, 0
        n = len(fruits)
        ans = 0
        my_dict = {}

        while r < n:
            my_dict[fruits[r]] = my_dict.get(fruits[r], 0) + 1

            if len(my_dict) > 2:
                    my_dict[fruits[l]] -= 1
                    if my_dict[fruits[l]] == 0:
                        del my_dict[fruits[l]]
                    l += 1
            else :
                ans = max(ans, r - l + 1)
            r += 1

        return ans
