class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 2D DP array with -1 (m rows × n columns)
        dp = [[-1 for col in range(n)] for row in range(m)]

        # Recursive helper function
        def solve(row, col, m, n, dp):
            # Base condition: if out of grid bounds
            if row >= m or col >= n:
                return 0
            
            # If destination (bottom-right corner) reached
            if row == (m - 1) and col == (n - 1):
                return 1
            
            # If already computed, return cached result (memoization)
            if dp[row][col] != -1:
                return dp[row][col]

            # Move right
            go_right = solve(row, col + 1, m, n, dp)
            # Move down
            go_down = solve(row + 1, col, m, n, dp)

            # Store result in DP table
            dp[row][col] = go_right + go_down

            # Return total unique paths from (row, col)
            return dp[row][col]

        # Start recursion from the top-left corner (0, 0)
        return solve(0, 0, m, n, dp)


# -----------------------------
# ✅ Time Complexity:
# O(m * n)
# Each cell (row, col) is computed once due to memoization.

# ✅ Space Complexity:
# O(m * n) for the DP table + O(m + n) recursion stack depth.
# -----------------------------
