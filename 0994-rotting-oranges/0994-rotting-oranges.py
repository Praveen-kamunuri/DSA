from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Get dimensions of the grid
        rows = len(grid)
        cols = len(grid[0])

        q = deque()  # Queue for BFS to hold positions of rotten oranges
        fresh_oranges = 0  # Count of fresh oranges

        # Step 1: Initialize the queue with all rotten oranges and count fresh ones...
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        mins = 0  # Minutes passed

        # Directions: right, down, up, left
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        # Step 2: BFS traversal to rot adjacent fresh oranges
        while q and fresh_oranges > 0:
            for i in range(len(q)):
                x, y = q.popleft()

                # Try all 4 adjacent cells
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    # If it's a valid fresh orange, rot it
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2  # Rot the orange
                        q.append((nx, ny))  # Add new rotten orange to queue
                        fresh_oranges -= 1  # Decrease fresh count

            mins += 1  # Increase time after each round of spreading

        # Step 3: Check if all oranges are rotten
        if fresh_oranges == 0:
            return mins
        else:
            return -1  # Not all oranges can be rotten

"""
\U0001f552 Time Complexity: O(m * n)
- Each cell is visited at most once, where m is the number of rows and n is the number of columns.

\U0001f9e0 Space Complexity: O(m * n)
- In worst case, the queue can hold all cells (if all are rotten or fresh), hence O(m * n) space.
"""
