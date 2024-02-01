class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col_seen = set()
        dia_seen = set()
        anti_seen = set()
        res = []
        empty_board = [["." for __ in range(n)] for __ in range(n)]
        def backtrack(row):
            if row == n:
                copy = ["".join(r) for r in empty_board]
                res.append(copy)
                return
            # col
            for col in range(n):
                diagonal = row-col
                anti_diagonal = row+col
                if col in col_seen or diagonal in dia_seen or anti_diagonal in anti_seen:
                    continue
                
                col_seen.add(col)
                dia_seen.add(diagonal)
                anti_seen.add(anti_diagonal)
                empty_board[row][col]="Q"

                backtrack(row+1)

                col_seen.remove(col)
                dia_seen.remove(diagonal)
                anti_seen.remove(anti_diagonal)
                empty_board[row][col]="."
                
            return False
                
        backtrack(0)


        return res