class Solution:
    def solve(self,idx,digits,mappings,result,subset):
        if idx == len(digits):
            result.append("".join(subset.copy()))
            return
        for i in range(len(mappings[int(digits[idx])])):
            subset.append(mappings[ int( digits[idx])][i])
            self.solve(idx + 1 , digits,mappings,result,subset)
            subset.pop()
    def letterCombinations(self, digits: str) -> List[str]:
        mappings = [0,0,"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        result = []
        self.solve(0,digits,mappings,result,[])
        return result
        