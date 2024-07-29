from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Function to solve the N-Queens problem recursively
        def solve(col, board, ans, leftrow, upperDia, lowerDia, n):
            # Base case: If all columns are filled, add the solution to the result
            if col == n:
                ans.append([''.join(row) for row in board])
                return

            # Iterate over each row in the current column
            for row in range(n):
                # Check if the current position is free in the row and diagonals
                if leftrow[row] == 0 and upperDia[row + col] == 0 and lowerDia[n - 1 + col - row] == 0:
                    # Place queen at the current position
                    board[row][col] = 'Q'
                    # Mark the row as occupied
                    leftrow[row] = 1
                    # Mark the upper diagonal as occupied
                    upperDia[row + col] = 1
                    # Mark the lower diagonal as occupied
                    lowerDia[n - 1 + col - row] = 1
                    # Recur to the next column
                    solve(col + 1, board, ans, leftrow, upperDia, lowerDia, n)
                    # Backtrack: Remove the queen from the current position
                    board[row][col] = '.'
                    # Mark the row as free
                    leftrow[row] = 0
                    # Undo the updates to diagonals
                    lowerDia[n - 1 + col - row] = 0
                    upperDia[row + col] = 0

        # Initialize variables for storing solutions and tracking queen positions
        ans = []
        board = [['.' for i in range(n)] for i in range(n)]
        leftrow = [0] * n
        upperDia = [0] * (2 * n - 1)
        lowerDia = [0] * (2 * n - 1)
        # Start solving the problem from the first column
        solve(0, board, ans, leftrow, upperDia, lowerDia, n)
        # Return the list of solutions
        return ans