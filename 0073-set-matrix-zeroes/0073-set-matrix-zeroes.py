class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        col = set()

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c]==0:
                    row.add(r)
                    col.add(c)

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in row or c in col:
                    matrix[r][c]=0
                    

        