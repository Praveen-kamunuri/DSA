class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize the triangle with the first two rows
        triangle = [[1], [1, 1]]
        
        # If numRows is 1, return the triangle with only the first row
        if numRows == 1:
            return [[1]]
        
        # If numRows is 2, return the triangle with the first two rows
        if numRows == 2:
            return [[1], [1, 1]]
        
        # Generate the remaining rows
        for i in range(numRows-2):
            row = [1]  # Start each row with 1
            
            # Calculate values for the current row based on the previous row
            for j in range(len(triangle[-1])-1):
                # Each value is the sum of the current and next element from the previous row
                row.append(triangle[-1][j]+triangle[-1][j+1])
            
            row.append(1)  # End each row with 1
            triangle.append(row)  # Add the row to the triangle
        
        return triangle
        