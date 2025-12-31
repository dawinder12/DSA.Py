def solve(self,idx,n,subset,result,open_count,close_count):
        if idx == 2 * n :
            if open_count == close_count :
                result.append("".join(subset.copy()))
                return
        if open_count <= n :
                subset.append("(")
                open_count += 1
                self.solve(idx + 1 , n , subset,result,open_count , close_count)
                subset.pop()
                open_count -= 1
        if close_count < open_count :
                subset.append(")")
                close_count += 1
                self.solve(idx + 1 , n ,subset,result,open_count,close_count)  
                close_count -=1
                subset.pop()              

def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.solve(0,n,[],result,0,0)
        return result