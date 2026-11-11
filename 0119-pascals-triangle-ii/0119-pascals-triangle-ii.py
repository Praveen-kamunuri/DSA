class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        # Store rowIndex in a shorter variable name n
        n = rowIndex

        # Base case: row 0 only contains [1]
        if n == 0:
            return [1]

        # Base case: row 1 contains [1, 1]
        if n == 1:
            return [1, 1]

        # Initialize the triangle with the first two rows (row 0 and row 1)
        triangle = [[1], [1, 1]]

        # Build each row starting from row 2 up to row n
        for i in range(2, n + 1):
            # Every row starts with 1
            row = [1]
            
            # Compute inner elements by summing the two numbers directly above in the previous row
            for j in range(1, i):
                ele = triangle[-1][j - 1] + triangle[-1][j]
                row.append(ele)
            
            # Every row ends with 1
            row.append(1)
            
            # Add the newly computed row to the triangle
            triangle.append(row)

        # Return a copy of the last generated row
        return triangle[-1][:]


# ==========================================
# Complexity Analysis:
# ==========================================
# Time Complexity: O(n^2)
#   - We iterate from row 2 to n.
#   - For each row i, the inner loop runs (i - 1) times.
#   - Total operations: 1 + 2 + 3 + ... + (n - 1) ≈ n(n - 1) / 2, which is O(n^2).
#
# Space Complexity: O(n^2)
#   - We store the entire triangle containing all rows from 0 to n.
#   - Total elements stored in memory: 1 + 2 + ... + (n + 1) ≈ (n + 1)(n + 2) / 2, which is O(n^2).
# ==========================================