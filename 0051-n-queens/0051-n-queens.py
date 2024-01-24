class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def solve(col, board, ans, leftrow, upperDia, lowerDia, n):
            if col == n:
                ans.append([''.join(row) for row in board])
                return

            for row in range(n):
                if leftrow[row] == 0 and upperDia[row + col] == 0 and lowerDia[n - 1 + col - row] == 0:
                    # Place queen
                    board[row][col] = 'Q'
                    leftrow[row] = 1
                    # Update upper diagonal
                    upperDia[row + col] = 1
                    # Update lower diagonal
                    lowerDia[n - 1 + col - row] = 1
                    # Recur to the next column
                    solve(col + 1, board, ans, leftrow, upperDia, lowerDia, n)
                    # Backtrack and remove the queen
                    board[row][col] = '.'
                    leftrow[row] = 0
                    # Undo the updates to diagonals
                    lowerDia[n - 1 + col - row] = 0
                    upperDia[row + col] = 0

        # Initialize variables
        ans = []
        board = [['.' for i in range(n)] for i in range(n)]
        leftrow = [0] * n
        upperDia = [0] * (2 * n - 1)
        lowerDia = [0] * (2 * n - 1)
        # Start solving from the first column
        solve(0, board, ans, leftrow, upperDia, lowerDia, n)
        return ans
