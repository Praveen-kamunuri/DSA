from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(row, col, grid, visited):

            visited[row][col] = 1
            q = deque()
            q.append((row,col))

            n = len(grid)
            m = len(grid[0])

            # 4-directional movement only
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while q:
                qrow, qcol = q.popleft()
                for dr, dc in directions:
                    nrow = qrow + dr
                    ncol = qcol + dc
                    if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == '1' and visited[nrow][ncol] == 0:
                        q.append((nrow, ncol))
                        visited[nrow][ncol] = 1

                            
        rows = len(grid)
        cols = len(grid[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        cnt = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and visited[row][col] != 1:
                    cnt += 1
                    bfs(row, col, grid, visited)

        return cnt
