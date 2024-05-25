from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Number of rows in the matrix
        n = len(matrix)
        # Number of columns in the matrix
        m = len(matrix[0])
        
        # Set the initial low and high pointers for binary search
        low = 0
        high = (m * n) - 1
        
        # Continue the search while the low pointer is less than or equal to the high pointer
        while low <= high:
            # Calculate the mid index
            mid = (low + high) // 2
            
            # Calculate the row and column indices corresponding to the mid index
            row = mid // m
            col = mid % m
            
            # Check if the target is found at the mid position
            if matrix[row][col] == target:
                return True
            # If the target is greater than the mid element, ignore the left half
            elif matrix[row][col] < target:
                low = mid + 1
            # If the target is less than the mid element, ignore the right half
            else:
                high = mid - 1
        
        # If the loop ends, the target is not present in the matrix
        return False
