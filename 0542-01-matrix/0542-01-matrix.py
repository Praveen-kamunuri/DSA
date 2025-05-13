from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        rows = len(mat)
        cols = len(mat[0])

        res = [[float('inf')] * cols for i in range(rows)]

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    res[r][c] = 0
                    q.append((r,c))

        directions = [(1,0), (0, -1), (-1,0), (0, 1)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if res[nr][nc] > res[r][c] + 1:
                        res[nr][nc] = res[r][c] + 1
                        q.append((nr, nc))

        return res



        