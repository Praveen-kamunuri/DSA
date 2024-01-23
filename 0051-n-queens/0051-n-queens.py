class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def solve(col, board, ans, leftrow, upperDia, lowerDia, n):
            if col == n:
                ans.append([''.join(row) for row in board])
                return

            for row in range(n):
                if leftrow[row] == 0 and upperDia[row + col] == 0 and lowerDia[n - 1 + col - row] == 0:
                    board[row][col] = 'Q'
                    leftrow[row] = 1
                    lowerDia[n - 1 + col - row] = 1  # Corrected this line
                    upperDia[row + col] = 1  # Corrected this line
                    solve(col + 1, board, ans, leftrow, upperDia, lowerDia, n)
                    board[row][col] = '.'
                    leftrow[row] = 0
                    lowerDia[n - 1 + col - row] = 0
                    upperDia[row + col] = 0

        ans = []
        board = [['.' for i in range(n)] for i in range(n)]
        leftrow = [0] * n
        upperDia = [0] * (2 * n - 1)
        lowerDia = [0] * (2 * n - 1)
        solve(0, board, ans, leftrow, upperDia, lowerDia, n)
        return ans
