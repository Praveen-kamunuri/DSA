class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        cols = len(board[0])

        visited = [['O'] * cols for i in range(rows)]

        directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

        def dfs(row = 0, col = 0):

            visited[row][col] = '1'

            for dr , dc in directions:
                nr, nc = row + dr , col + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc] == 'O' and visited[nr][nc] == 'O':
                        dfs(nr, nc)

        # Top row to righ side
        for col in range(cols):
            if board[0][col] == 'O':
                dfs(col = col)



        # Right column (excluding top and bottom)
        for row in range(1, rows - 1):
            if board[row][cols - 1] == 'O':
                dfs(row = row, col = cols - 1)


        # Bottom row (if there is more than one row)
        if rows > 1:
            for col in range(cols - 1, -1, -1):
                if board[rows - 1][col] == 'O':
                    dfs(row = rows - 1, col = col)
        # Left column (excluding top and bottom)
        for row in range(rows - 2, 0, -1):
            if board[row][0] == 'O':
                dfs(row = row)


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and visited[r][c] == 'O':
                    board[r][c] = 'X'
        
