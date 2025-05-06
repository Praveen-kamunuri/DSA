from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        count_fresh = 0

        # Step 1: Count fresh oranges and collect rotten ones
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    count_fresh += 1

        if count_fresh == 0:
            return 0

        minutes = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Step 2: BFS to rot adjacent fresh oranges
        while queue and count_fresh > 0:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        count_fresh -= 1
            minutes += 1

        return minutes if count_fresh == 0 else -1
