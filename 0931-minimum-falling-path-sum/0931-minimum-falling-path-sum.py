import sys
from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        # ==========================================================
        # APPROACH 1: PURE RECURSION (TOP-DOWN)
        #
        # Idea:
        # f(row, col) = minimum path sum to reach (row, col)
        # From (row, col) we can come from:
        #   (row-1, col), (row-1, col-1), (row-1, col+1)
        #
        # TC: Exponential ~ O(3^n)
        # SC: O(n) recursion stack
        # ==========================================================
        '''
        def find_min_path(row, col):
            if col < 0 or col >= n:
                return sys.maxsize
            if row == 0:
                return matrix[0][col]

            up = matrix[row][col] + find_min_path(row - 1, col)
            left_diag = matrix[row][col] + find_min_path(row - 1, col - 1)
            right_diag = matrix[row][col] + find_min_path(row - 1, col + 1)

            return min(up, left_diag, right_diag)

        ans = sys.maxsize
        for col in range(n):
            ans = min(ans, find_min_path(n - 1, col))
        return ans
        '''

        # ==========================================================
        # APPROACH 2: MEMOIZATION (TOP-DOWN DP)
        #
        # Idea:
        # Same recursion, store results in dp[row][col]
        #
        # TC: O(n^2)
        # SC: O(n^2) + O(n) recursion stack
        # ==========================================================
        '''
        dp = [[-1 for _ in range(n)] for _ in range(n)]

        def find_min_path(row, col):
            if col < 0 or col >= n:
                return sys.maxsize
            if row == 0:
                return matrix[0][col]
            if dp[row][col] != -1:
                return dp[row][col]

            up = matrix[row][col] + find_min_path(row - 1, col)
            left_diag = matrix[row][col] + find_min_path(row - 1, col - 1)
            right_diag = matrix[row][col] + find_min_path(row - 1, col + 1)

            dp[row][col] = min(up, left_diag, right_diag)
            return dp[row][col]

        ans = sys.maxsize
        for col in range(n):
            ans = min(ans, find_min_path(n - 1, col))
        return ans
        '''

        # ==========================================================
        # APPROACH 3: TABULATION (BOTTOM-UP DP)
        #
        # Idea:
        # dp[row][col] = min path sum to reach (row, col)
        #
        # TC: O(n^2)
        # SC: O(n^2)
        # ==========================================================
        '''
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for col in range(n):
            dp[0][col] = matrix[0][col]

        for row in range(1, n):
            for col in range(n):
                if col == 0:
                    dp[row][col] = matrix[row][col] + min(
                        dp[row - 1][col],
                        dp[row - 1][col + 1]
                    )
                elif col == n - 1:
                    dp[row][col] = matrix[row][col] + min(
                        dp[row - 1][col],
                        dp[row - 1][col - 1]
                    )
                else:
                    dp[row][col] = matrix[row][col] + min(
                        dp[row - 1][col],
                        dp[row - 1][col - 1],
                        dp[row - 1][col + 1]
                    )

        return min(dp[n - 1])
        '''

        # ==========================================================
        # APPROACH 4: SPACE OPTIMIZED DP (BEST / SUBMITTED)
        #
        # Idea:
        # Only previous row is needed at any time
        #
        # TC: O(n^2)
        # SC: O(n)
        # ==========================================================

        prev = matrix[0][:]

        for row in range(1, n):
            temp = [0] * n
            for col in range(n):
                if col == 0:
                    temp[col] = matrix[row][col] + min(prev[col], prev[col + 1])
                elif col == n - 1:
                    temp[col] = matrix[row][col] + min(prev[col], prev[col - 1])
                else:
                    temp[col] = matrix[row][col] + min(
                        prev[col],
                        prev[col - 1],
                        prev[col + 1]
                    )
            prev = temp

        return min(prev)
