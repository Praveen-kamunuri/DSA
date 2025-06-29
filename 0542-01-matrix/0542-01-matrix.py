from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Get the size of the matrix
        rows = len(mat)
        cols = len(mat[0])

        # Initialize the result matrix with infinity
        res = [[float('inf')] * cols for _ in range(rows)]

        # Queue for BFS
        q = deque()

        # Step 1: Add all 0s to the queue and set their distance as 0 in result
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    res[r][c] = 0
                    q.append((r, c))  # Start BFS from 0s

        # Define 4 possible directions (down, left, up, right)
        directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

        # Step 2: Perform BFS to update distances
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # If within bounds and the new cell has not been visited or found a shorter distance
                if 0 <= nr < rows and 0 <= nc < cols:
                    if res[nr][nc] > res[r][c] + 1:
                        res[nr][nc] = res[r][c] + 1
                        q.append((nr, nc))

        return res

# ✅ Time Complexity: O(m * n)
#   - Each cell is visited at most once during BFS.
#   - m = number of rows, n = number of columns.

# ✅ Space Complexity: O(m * n)
#   - res matrix takes O(m * n)
#   - queue can hold up to O(m * n) elements in worst case.
