class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[-1 for _ in range(n)]for _ in range(m)]


        def cal_paths(row, col, m, n, dp):

            if row == (m - 1) and col == (n - 1):
                return 1

            if row < m and col < n:

                if dp[row][col] != -1:
                    return dp[row][col]
                
                go_down = cal_paths(row + 1, col, m, n, dp)
                go_right = cal_paths(row, col + 1, m, n, dp)

                dp[row][col] = go_down + go_right

                return dp[row][col]

            else:
                return 0

        return cal_paths(0, 0, m, n, dp)


          