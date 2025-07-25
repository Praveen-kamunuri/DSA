import sys
from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # If the starting point is blocked, return -1
        if grid[0][0] == 1:
            return -1

        rows = len(grid)
        cols = len(grid[0])

        # If grid is 1x1 and the only cell is open
        if rows == 1 and cols == 1:
            return 1

        # Initialize the distance matrix with infinity
        distance = [[sys.maxsize for _ in range(cols)] for _ in range(rows)]

        # Queue for BFS: stores (distance, (row, col))
        q = deque()
        q.append((0, (0, 0)))  # Start from top-left corner

        # Mark starting cell's distance as 0
        distance[0][0] = 0

        # 8 possible directions: up, down, left, right, and diagonals
        del_row = [-1, 1, 0, 0, -1, 1, 1, -1]
        del_col = [0, 0, -1, 1, 1, 1, -1, -1]

        while q:
            dist, (row, col) = q.popleft()

            # Check all 8 neighbors
            for i in range(8):
                new_row = row + del_row[i]
                new_col = col + del_col[i]

                # Ensure new cell is within bounds and open (0), and this is a shorter path
                if (0 <= new_row < rows and 0 <= new_col < cols and 
                    grid[new_row][new_col] == 0 and 
                    dist + 1 < distance[new_row][new_col]):

                    distance[new_row][new_col] = dist + 1

                    # If destination is reached (bottom-right cell)
                    if new_row == rows - 1 and new_col == cols - 1:
                        return dist + 2  # +2 accounts for start + move

                    q.append((dist + 1, (new_row, new_col)))

        # If destination not reachable
        return -1

"""
Time Complexity (TC): O(N * M)
- Every cell is visited at most once.
- Each cell explores up to 8 directions (constant factor).

Space Complexity (SC): O(N * M)
- Distance matrix stores one value per cell.
- Queue can hold up to N*M elements in worst case.
"""
