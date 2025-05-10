from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        result = [[float('inf')] * cols for _ in range(rows)]
        queue = deque()

        # Add all 0s to the queue and set their distance as 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    result[r][c] = 0
                    queue.append((r, c))

        # Directions: up, down, left, right
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # BFS
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < rows and 0 <= new_c < cols:
                    if result[new_r][new_c] > result[r][c] + 1:
                        result[new_r][new_c] = result[r][c] + 1
                        queue.append((new_r, new_c))

        return result
