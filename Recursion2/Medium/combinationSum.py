def solve(self,idx , n , subset , result,target,total,candidates): # tc - > O(n * 2 ^k)
        if idx == n :
            if total == target :
                result.append(subset.copy())
            return
        if total > target :
            return
        if total == target :
            result.append(subset.copy())
            return
        total += candidates[idx]
        subset.append(candidates[idx])
        self.solve(idx , n , subset,result,target,total,candidates)
        total -= candidates[idx]
        subset.pop()
        self.solve(idx + 1 , n ,subset,result,target,total,candidates)

def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.solve(0,len(candidates) , [] , result , target,0,candidates)
        return result
        
        