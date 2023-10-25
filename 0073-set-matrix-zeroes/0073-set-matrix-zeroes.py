class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        zero_rows = []
        zero_cols = []
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.append(i)
                    zero_cols.append(j)
        for i in range(rows):
            for j in range(cols):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0
        
        