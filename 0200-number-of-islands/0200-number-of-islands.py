from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Helper function to perform BFS traversal from a given cell
        def bfs(row, col, grid, visited):
            # Mark the starting cell as visited
            visited[row][col] = 1
            q = deque()
            q.append((row, col))

            n = len(grid)
            m = len(grid[0])

            # Define the 4 possible directions: up, down, left, right
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            # Start BFS
            while q:
                qrow, qcol = q.popleft()

                for dr, dc in directions:
                    nrow = qrow + dr
                    ncol = qcol + dc

                    # Check if the neighbor is within bounds, is land, and not visited
                    if (0 <= nrow < n and 0 <= ncol < m and 
                        grid[nrow][ncol] == '1' and visited[nrow][ncol] == 0):
                        q.append((nrow, ncol))
                        visited[nrow][ncol] = 1  # Mark neighbor as visited

        rows = len(grid)
        cols = len(grid[0])

        # Create a visited matrix initialized with 0s
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        cnt = 0  # Count of islands

        # Traverse each cell in the grid
        for row in range(rows):
            for col in range(cols):
                # If the cell is land and not visited, it's a new island
                if grid[row][col] == '1' and visited[row][col] == 0:
                    cnt += 1
                    bfs(row, col, grid, visited)  # Start BFS from this cell

        return cnt  # Return total number of islands


# Time Complexity: O(n * m)
#   - Each cell is visited at most once in the BFS traversal.
#
# Space Complexity: O(n * m)
#   - visited matrix takes O(n * m) space.
#   - In worst case, the queue may also store O(n * m) cells during BFS.