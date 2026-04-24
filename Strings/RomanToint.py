class Solution:
    def solve(self, i, s, mp):
        if i >= len(s):
            return 0
        if i + 1 < len(s) and mp[s[i]] < mp[s[i+1]]:
            return -mp[s[i]] + self.solve(i + 1, s, mp)
        return mp[s[i]] + self.solve(i + 1, s, mp)

    def romanToInt(self, s: str) -> int:
        mp = {
            "I":1, "V":5, "X":10,
            "L":50, "C":100,
            "D":500, "M":1000
        }
        return self.solve(0, s, mp)