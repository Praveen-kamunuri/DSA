from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        q = deque()

        fresh_oranges = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    q.append((i,j))

        mins = 0

        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        while q and fresh_oranges > 0:
            for i in range(len(q)):
                x, y = q.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        q.append((nx,ny))
                        fresh_oranges -= 1
            mins += 1
        
        if fresh_oranges == 0:
            return mins
        else:
            return -1

