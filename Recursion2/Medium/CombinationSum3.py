def solve(self,idx,k,n,digits,total,subset,result):
        if digits > k :
            return
        if digits == k and total == n :
            result.add(tuple(subset.copy()))
        if idx > 9 :
            return
        total += idx
        digits += 1
        subset.append(idx)
        self.solve(idx + 1 , k , n ,digits , total , subset,result)
        total -= idx
        digits -= 1
        subset.pop()
        self.solve(idx + 1 , k ,n , digits,total , subset,result)

def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n > 45 :
            return []
        if n == 45 :
            return [[1,2,3,4,5,6,7,8,9]]
        result = set()
        digits = 0
        self.solve(1,k,n,digits,0,[],result)
        return list(result)