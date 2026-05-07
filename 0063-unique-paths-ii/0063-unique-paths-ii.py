class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[-1 for _ in range(n)]for _ in range(m)]


        def find_paths(row, col, m, n, dp):
            if row == 0 and col == 0:
                return 1

            if row < 0 or col < 0:
                return 0

            if obstacleGrid[row][col] != 1:

                if dp[row][col] != -1:
                    return dp[row][col]

                go_up = find_paths(row - 1, col, m, n, dp)
                go_left = find_paths(row, col - 1, m, n, dp)

                dp[row][col] = go_up + go_left

                return dp[row][col]
            else:
                return 0
            
        return find_paths(m - 1, n - 1, m, n, dp)
        