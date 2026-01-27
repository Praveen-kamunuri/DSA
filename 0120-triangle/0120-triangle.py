import sys
from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        """
        --------------------------------------------------
        APPROACH 1: PURE RECURSION (Top-Down)
        --------------------------------------------------
        Idea:
        - From each cell, you can go:
            1. Down
            2. Down-Right (Diagonal)
        - Try both paths and take minimum

        Time Complexity: O(2^n)   (Exponential, overlapping subproblems)
        Space Complexity: O(n)    (Recursion stack)

        ❌ TLE for large inputs
        """

        # def solve_triangle(row, col):
        #     if row == len(triangle) - 1:
        #         return triangle[row][col]
        #
        #     go_down = triangle[row][col] + solve_triangle(row + 1, col)
        #     go_diag = triangle[row][col] + solve_triangle(row + 1, col + 1)
        #
        #     return min(go_down, go_diag)
        #
        # return solve_triangle(0, 0)



        """
        --------------------------------------------------
        APPROACH 2: RECURSION + MEMOIZATION (Top-Down DP)
        --------------------------------------------------
        Idea:
        - Same recursion
        - Store results of (row, col) to avoid recomputation

        Time Complexity: O(n^2)
        Space Complexity: O(n^2) DP + O(n) recursion stack
        """

        # m = len(triangle)
        # dp = [[-1 for _ in range(m)] for _ in range(m)]
        #
        # def solve_triangle(row, col):
        #     if row == m - 1:
        #         return triangle[row][col]
        #
        #     if dp[row][col] != -1:
        #         return dp[row][col]
        #
        #     go_down = triangle[row][col] + solve_triangle(row + 1, col)
        #     go_diag = triangle[row][col] + solve_triangle(row + 1, col + 1)
        #
        #     dp[row][col] = min(go_down, go_diag)
        #     return dp[row][col]
        #
        # return solve_triangle(0, 0)



        """
        --------------------------------------------------
        APPROACH 3: TABULATION (Bottom-Up DP)
        --------------------------------------------------
        Idea:
        - Build dp table row by row
        - dp[row][col] = min path sum to reach that cell

        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        """

        # m = len(triangle)
        # dp = [[0] * (row + 1) for row in range(m)]
        #
        # dp[0][0] = triangle[0][0]
        #
        # for row in range(1, m):
        #     for col in range(row + 1):
        #         if col == 0:
        #             dp[row][col] = triangle[row][col] + dp[row - 1][col]
        #         elif col == row:
        #             dp[row][col] = triangle[row][col] + dp[row - 1][col - 1]
        #         else:
        #             dp[row][col] = triangle[row][col] + min(
        #                 dp[row - 1][col],
        #                 dp[row - 1][col - 1]
        #             )
        #
        # return min(dp[m - 1])



        """
        --------------------------------------------------
        APPROACH 4: SPACE OPTIMIZED DP (Bottom-Up) ✅ FINAL
        --------------------------------------------------
        Idea:
        - Only previous row is needed at any time
        - Reduce space from O(n^2) → O(n)

        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """

        rows = len(triangle)

        # Stores dp of previous row
        prev = [0] * len(triangle[-1])
        prev[0] = triangle[0][0]

        for i in range(1, rows):
            cols = i + 1
            temp = [0] * cols

            for j in range(cols):
                if j == 0:
                    temp[j] = triangle[i][j] + prev[j]
                elif j == i:
                    temp[j] = triangle[i][j] + prev[j - 1]
                else:
                    temp[j] = triangle[i][j] + min(prev[j], prev[j - 1])

            prev = temp

        # Answer is minimum in last row
        return min(prev)
