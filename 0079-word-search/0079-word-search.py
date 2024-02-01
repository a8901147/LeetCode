class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row,col,i):
            if i == len(word):
                return True
                
            if row<0 or row>=len(board) or col<0 or col>=len(board[0]) or board[row][col]!=word[i] or (row,col) in seen:
                return False
            seen.add((row,col))
            dirs=[[1,0],[-1,0],[0,1],[0,-1]]
            for r,c in dirs:
                if dfs(row+r,col+c,i+1):
                    return True
            seen.remove((row,col))
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                seen = set()
                if dfs(row,col,0):
                    return True
        return False