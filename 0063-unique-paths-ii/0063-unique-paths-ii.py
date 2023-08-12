class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # Create a 2D array to store the number of unique paths to each cell
        dp = [[0] * n for _ in range(m)]

        # Initialize the first cell
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        # Initialize the first column
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] if obstacleGrid[i][0] == 0 else 0

        # Initialize the first row
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] if obstacleGrid[0][j] == 0 else 0

        # Fill in the rest of the dp array
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]

  




