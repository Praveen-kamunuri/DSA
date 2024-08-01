from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        def findPeakRec(mat, startCol, endCol):
            midCol = (startCol + endCol) // 2
            maxRow = 0
            for row in range(len(mat)):
                if mat[row][midCol] > mat[maxRow][midCol]:
                    maxRow = row
            
            # Check neighbors
            if (midCol - 1 >= 0 and mat[maxRow][midCol] < mat[maxRow][midCol - 1]):
                # Move to the left half
                return findPeakRec(mat, startCol, midCol - 1)
            elif (midCol + 1 < len(mat[0]) and mat[maxRow][midCol] < mat[maxRow][midCol + 1]):
                # Move to the right half
                return findPeakRec(mat, midCol + 1, endCol)
            else:
                # Peak element found
                return [maxRow, midCol]
        
        return findPeakRec(mat, 0, len(mat[0]) - 1)
