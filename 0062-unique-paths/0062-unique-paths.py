class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[-1 for _ in range(n)]for _ in range(m)]
        def cal_paths(row, col, m, n):
            if row == 0 and col == 0:
                return 1


            if row < 0 or col < 0:
                return 0

            if dp[row][col] != -1:
                return dp[row][col]

            go_up = cal_paths(row - 1, col, m, n)
            go_left = cal_paths(row, col - 1, m, n)

            dp[row][col] = go_up + go_left

            return dp[row][col]
    
        return cal_paths(m - 1, n -1, m, n)
        