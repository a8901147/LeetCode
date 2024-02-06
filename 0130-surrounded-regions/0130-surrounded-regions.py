class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(row,col):
            if row<0 or col<0 or row>=len(board) or col>=len(board[0]) or board[row][col]=="X" or (row,col) in seen:
                return 
            board[row][col] = "T"
            seen.add((row,col))
            dirs = [[1,0],[-1,0],[0,1],[0,-1]]
            for x, y in dirs:
                dfs(row+x,col+y)
        
        seen = set()
        for col in range(len(board[0])):
            dfs(0,col)
            dfs(len(board)-1,col)

        for row in range(len(board)):
            dfs(row,0)
            dfs(row,len(board[0])-1)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "T":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"
        