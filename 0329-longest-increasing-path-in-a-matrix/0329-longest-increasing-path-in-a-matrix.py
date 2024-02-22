class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        def dfs(r,c,prev):
            if r<0 or c<0 or r>=len(matrix) or c>=len(matrix[0]) or (r,c) in seen or matrix[r][c]<=prev:
                return 0
            
            if (r,c) in path_map:
                return path_map[(r,c)]
            
            seen.add((r,c))
            dirs = [[1,0],[-1,0],[0,1],[0,-1]]
            max_path = 0
            for x, y in dirs:
                next_row, next_col = r+x, c+y
                max_path = max(max_path,dfs(r+x,c+y,matrix[r][c]))
            seen.remove((r,c))
            path_map[(r,c)] = max_path+1
            return max_path+1

        res = 0
        path_map = {}
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                seen = set()
                res = max(res,dfs(r,c,-1))
        
        return res