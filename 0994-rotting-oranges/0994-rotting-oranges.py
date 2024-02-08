class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rottens = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                state = grid[r][c]
                if state == 1:
                    fresh += 1
                elif state == 2:
                    rottens.append([r,c])
        
        counter = 0

        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        while rottens and fresh:
            next_rottens = []
            for rotten_x, rotten_y in rottens:
                for x, y in dirs:
                    orange_x = rotten_x + x
                    orange_y = rotten_y + y
                    if orange_x < 0 or orange_x >= len(grid) or orange_y<0 or orange_y>=len(grid[0]) or grid[orange_x][orange_y]!=1:
                        continue
                    fresh -= 1
                    grid[orange_x][orange_y] = 2
                    next_rottens.append([orange_x,orange_y])
            if next_rottens:
                counter += 1
            rottens = next_rottens

        return counter if fresh == 0 else -1
