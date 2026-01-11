class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        prev = [0] * n
        prev[0] = grid[0][0]
        
        for j in range(1, n):
            prev[j] = prev[j - 1] + grid[0][j]
        
        print(prev)
        
        for i in range(1, m):
            temp = [0] * n
            for j in range(n):
                if j == 0:
                    temp[j] = grid[i][j] + prev[j]
                else:
                    temp[j] = grid[i][j] + min(temp[j - 1], prev[j])
            prev = temp
        return prev[n - 1]