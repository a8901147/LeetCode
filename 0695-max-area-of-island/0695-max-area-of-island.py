class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        seen = set()
        rowSize = len(grid)
        colSize = len(grid[0])
        def dfs(r,c):
            if r < 0 or r == rowSize or c < 0 or c == colSize or (r,c) in seen or grid[r][c] == 0:
                return 0
            seen.add((r,c))
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1) 

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                res = max(res,dfs(r,c))
 
        return res
