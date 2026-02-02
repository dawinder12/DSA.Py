class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_dict = {}
        l,r = 0,0
        ans = 0
        while r < len(s) :
            if s[r] in my_dict :
                l = max(l,my_dict[s[r]] + 1)
            my_dict[s[r]] = r
            ans = max(ans,r - l + 1)
            r += 1
        return ans




        