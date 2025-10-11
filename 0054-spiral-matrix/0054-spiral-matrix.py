class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)  # Number of rows
        m = len(matrix[0])  # Number of columns

        top = 0  # Initialize the top row
        left = 0  # Initialize the leftmost column
        bottom = n - 1  # Initialize the bottom row
        right = m - 1  # Initialize the rightmost column

        ans = []  # Initialize the result list to store the spiral order

        while top <= bottom and left <= right:
            # Traverse the top row from left to right and append elements to ans
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            # Traverse the rightmost column from top to bottom and append elements to ans
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            # Check if there's a bottom row to traverse
            if top <= bottom:
                # Traverse the bottom row from right to left and append elements to ans
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            # Check if there's a leftmost column to traverse
            if left <= right:
                # Traverse the leftmost column from bottom to top and append elements to ans
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1

        return ans  # Return the list containing elements in spiral order
