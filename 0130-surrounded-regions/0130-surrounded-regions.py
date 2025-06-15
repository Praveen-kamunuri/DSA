class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        The function modifies the board in place, changing all 'O' regions
        that are surrounded by 'X' into 'X' and leaving 'O' regions connected to
        the border unchanged..
        """

        rows = len(board)  # Get number of rows in the board..
        cols = len(board[0])  # Get number of columns in the board

        # Initialize a visited matrix to track cells we've already processed
        visited = [['O'] * cols for i in range(rows)]  # Initially, all are unvisited ('O')

        # Directions to check: down, left, up, right
        directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

        def dfs(row=0, col=0):
            """
            Perform Depth First Search to mark all connected 'O' starting from the 
            given row, col. We mark the visited cells to prevent revisiting.
            """
            # Mark the current cell as visited
            visited[row][col] = '1'

            # Explore all 4 possible directions
            for dr, dc in directions:
                nr, nc = row + dr, col + dc  # Calculate the next row and column

                # Check if the next cell is within the board bounds and is an 'O'
                if 0 <= nr < rows and 0 <= nc < cols:
                    # If the cell is 'O' and hasn't been visited yet, perform DFS
                    if board[nr][nc] == 'O' and visited[nr][nc] == 'O':
                        dfs(nr, nc)

        # Start DFS from the top row, checking each column
        for col in range(cols):
            if board[0][col] == 'O':  # Check top row
                dfs(row=0, col=col)  # Explicitly pass col for clarity (not mandatory but readable)

        # Start DFS from the right column (excluding corners)
        for row in range(1, rows - 1):  # Avoid top and bottom rows
            if board[row][cols - 1] == 'O':  # Check right column
                dfs(row=row, col=cols - 1)  # Explicitly pass col for clarity

        # Start DFS from the bottom row, checking each column (excluding corners)
        if rows > 1:
            for col in range(cols - 1, -1, -1):  # Iterate backward to check bottom row
                if board[rows - 1][col] == 'O':  # Check bottom row
                    dfs(row=rows - 1, col=col)  # Explicitly pass col for clarity

        # Start DFS from the left column (excluding corners)
        for row in range(rows - 2, 0, -1):  # Avoid top and bottom rows
            if board[row][0] == 'O':  # Check left column
                dfs(row=row, col=0)  # Explicitly pass col for clarity

        # Post DFS: change all unvisited 'O' to 'X' (they are surrounded by 'X')
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and visited[r][c] == 'O':
                    board[r][c] = 'X'  # Mark the surrounded 'O' as 'X'


# Time Complexity: 
# - The DFS function will visit each cell once in the worst case.
# - Thus, the time complexity is O(m * n), where m is the number of rows and n is the number of columns.

# Space Complexity:
# - The visited matrix takes O(m * n) space, where m is the number of rows and n is the number of columns.
# - The recursive call stack of DFS will also take O(m * n) space in the worst case.
# Therefore, the total space complexity is O(m * n).

