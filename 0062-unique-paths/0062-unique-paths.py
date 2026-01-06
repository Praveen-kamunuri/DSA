class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0 for _ in range(n)]for _ in range(m)]

        dp[0][0] = 1
        
        for i in range(0, m):
            for j in range(0, n):

                if i == 0 and j == 0:
                    continue
                else:
                    go_up = dp[i - 1][j]
                    go_right = dp[i][j - 1]

                    dp[i][j] = go_up + go_right

        return dp[m - 1][n - 1]
        