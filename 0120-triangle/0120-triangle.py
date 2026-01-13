class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        m = len(triangle)

        dp = [[-1 for _ in range(m)]for _ in range(m)]

        def solve_triangle(row, col, m, dp):

            if row == m - 1:
                return triangle[row][col]
            
            if dp[row][col] != -1:
                return dp[row][col]

            go_down = triangle[row][col] + solve_triangle(row + 1, col, m, dp)
            go_diagonal = triangle[row][col] + solve_triangle(row + 1, col + 1, m, dp)

            dp[row][col] = min(go_down, go_diagonal)

            return dp[row][col]

        return solve_triangle(0, 0, m, dp)