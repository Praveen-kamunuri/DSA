from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Get the number of rows and columns in the original matrix
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Initialize the result matrix with dimensions swapped (cols x rows)
        res = [[0] * rows for i in range(cols)]
        
        # Iterate through each element of the original matrix
        for i in range(rows):
            for j in range(cols):
                # Transpose the element from the original matrix to the result matrix
                # Swap the indices to achieve the transpose effect
                res[j][i] = matrix[i][j]
        
        # Return the transposed matrix
        return res

    