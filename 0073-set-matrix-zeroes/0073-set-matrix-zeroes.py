class Solution(object):
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        
        zeroRows = set()
        zeroCols = set()
        
        # Identify the rows and columns containing zeros
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zeroRows.add(i)
                    zeroCols.add(j)
        
        # Set the corresponding rows and columns to zeros
        for i in range(rows):
            for j in range(cols):
                if i in zeroRows or j in zeroCols:
                    matrix[i][j] = 0
        
        return matrix
