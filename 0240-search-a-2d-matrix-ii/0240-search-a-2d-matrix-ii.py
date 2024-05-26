class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)      # Number of rows in the matrix
        m = len(matrix[0])   # Number of columns in the matrix
        
        row = 0              # Start from the first row
        col = m - 1          # Start from the last column
        
        # Loop to traverse the matrix
        while row < n and col >= 0:
            if matrix[row][col] == target:
                return True  # Target found
            
            elif matrix[row][col] < target:
                row += 1     # Move down to the next row if the current element is less than the target
                
            else:
                col -= 1     # Move left to the previous column if the current element is greater than the target
                
        return False         # Target not found after traversing the matrix

# Time Complexity: O(M + N)
# Space Complexity: O(1)

# Explanation:
# - M is the number of rows in the matrix.
# - N is the number of columns in the matrix.
# - The algorithm starts from the top-right corner and moves left or down based on the comparison.
# - In the worst case, it will move through at most M rows and N columns, giving a time complexity of O(M + N).
# - Space complexity is O(1) because we are not using any additional space that scales with the input size.
