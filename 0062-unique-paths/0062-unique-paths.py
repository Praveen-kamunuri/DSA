class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # dp[i][j] represents number of unique paths
        # to reach cell (i, j) from (0, 0)
        # Space Complexity: O(m * n) → 2D DP table
        dp = [[0 for _ in range(n)]for _ in range(m)]

        # Base case: only 1 way to start at (0, 0)
        dp[0][0] = 1
        
        # Time Complexity:
        # Two nested loops running over m rows and n columns
        # TC = O(m * n)
        for i in range(0, m):
            for j in range(0, n):

                # Skip starting cell as it is already initialized
                if i == 0 and j == 0:
                    continue
                else:
                    # Number of ways from top cell
                    go_up = dp[i - 1][j]

                    # Number of ways from left cell
                    go_right = dp[i][j - 1]

                    # Total ways to reach current cell
                    dp[i][j] = go_up + go_right

        # Answer is stored in bottom-right cell
        return dp[m - 1][n - 1]
