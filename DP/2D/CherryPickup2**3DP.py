# class Solution:
#     def solve(self,i,j1,j2,grid,dp):
#         if i >= len(grid) or j1 < 0 or j2 < 0 or j1 >= len(grid[0]) or j2>=len(grid[0]):
#             return float("-inf")
#         if i == len(grid) - 1 :
#             if j1 == j2 :
#                 return grid[i][j1] # return only one
#             return grid[i][j1] + grid[i][j2] # if both are diff select both
#         if dp[i][j1][j2] != - 1 :
#             return dp[i][j1][j2]
#         maxi = 0
#         for dj1 in range(-1,2): # -1 0 1
#             for dj2 in range(-1,2): # total 9 cases
#                 if j1 == j2 :
#                     value = grid[i][j1] + self.solve(i+1,j1+dj1,j2+dj2,grid,dp)
#                 else :
#                     value = grid[i][j1] + grid[i][j2] + self.solve(i+1,j1+dj1,j2+dj2,grid,dp)
#                 maxi = max(maxi,value)
#         dp[i][j1][j2] = maxi
#         return maxi      
#     def cherryPickup(self, grid: List[List[int]]) -> int:
#         rows = len(grid)
#         cols = len(grid[0])
#         dp = [[[-1 for _ in range(cols)] for _ in range(cols)] for _ in range(rows)]
#         return self.solve(0,0,cols-1,grid,dp)


class Solution:  
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[[-1 for _ in range(cols)] for _ in range(cols)] for _ in range(rows)]
        for j1 in range(cols):
            for j2 in range(cols):
                if j1 == j2 :
                    dp[0][j1][j2] = grid[rows - 1][j1]
                    continue
                dp[rows - 1 ][j1][j2] = grid[rows - 1][j1] + grid[rows - 1][j2]
        for i in range(rows-2,-1,-1):
            for j1 in range(cols):
                for j2 in range(cols):
                    maxi = 0
                    for dj1 in range(-1,2): # -1 0 1
                        for dj2 in range(-1,2): # total 9 cases
                            if j1 == j2 :
                                value = grid[i][j1]
                            else :
                                value = grid[i][j1] + grid[i][j2]
                            if j1 + dj1 < 0 or j2 + dj2 < 0 or j1 +dj1 >= cols or j2 + dj2 >= cols or i +1 >= rows:
                                value += float("-inf")
                            else :
                                value += dp[i+1][j1+dj1][j2+dj2]
                            maxi = max(maxi,value)
                    dp[i][j1][j2] = maxi
        return dp[0][0][cols-1]

                    
                        
        