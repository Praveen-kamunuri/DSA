class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # =====================================================
        # 1️⃣ RECURSION (Brute Force) ❌ TLE
        # =====================================================
        """
        Idea:
        - From cell (i, j), you can come from:
            - top (i-1, j)
            - left (i, j-1)
        - Choose minimum path sum

        Base cases:
        - If (i, j) == (0, 0) → return grid[0][0]
        - If out of bounds → return large value

        TC: Exponential (2^(m+n))
        SC: O(m+n) recursion stack
        """

        # def solve(i, j):
        #     if i == 0 and j == 0:
        #         return grid[0][0]
        #
        #     if i < 0 or j < 0:
        #         return 10**9
        #
        #     up = solve(i - 1, j)
        #     left = solve(i, j - 1)
        #
        #     return grid[i][j] + min(up, left)
        #
        # return solve(m - 1, n - 1)

        # =====================================================
        # 2️⃣ MEMOIZATION (Top-Down DP)
        # =====================================================
        """
        Optimization over recursion:
        - Store already computed results in dp table

        dp[i][j] = minimum path sum to reach cell (i, j)

        TC: O(m * n)
        SC: O(m * n) dp array + O(m+n) recursion stack
        """

        # dp = [[-1 for _ in range(n)] for _ in range(m)]
        #
        # def solve(i, j):
        #     if i == 0 and j == 0:
        #         return grid[0][0]
        #
        #     if i < 0 or j < 0:
        #         return 10**9
        #
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #
        #     up = solve(i - 1, j)
        #     left = solve(i, j - 1)
        #
        #     dp[i][j] = grid[i][j] + min(up, left)
        #     return dp[i][j]
        #
        # return solve(m - 1, n - 1)

        # =====================================================
        # 3️⃣ TABULATION (Bottom-Up DP)
        # =====================================================
        """
        Convert recursion to iteration

        dp[i][j] = minimum path sum to reach (i, j)

        TC: O(m * n)
        SC: O(m * n)
        """

        # dp = [[0 for _ in range(n)] for _ in range(m)]
        #
        # dp[0][0] = grid[0][0]
        #
        # # first row
        # for j in range(1, n):
        #     dp[0][j] = dp[0][j - 1] + grid[0][j]
        #
        # # first column
        # for i in range(1, m):
        #     dp[i][0] = dp[i - 1][0] + grid[i][0]
        #
        # # remaining cells
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        #
        # return dp[m - 1][n - 1]

        # =====================================================
        # 4️⃣ SPACE OPTIMIZATION ✅ (FINAL SUBMISSION)
        # =====================================================
        """
        Observation:
        - To compute current row, we only need:
            - previous row
            - current row's left value

        So instead of 2D dp, use 1D array

        prev[j] = minimum path sum to reach column j of previous row

        TC: O(m * n)
        SC: O(n)
        """

        prev = [0] * n
        prev[0] = grid[0][0]

        # initialize first row
        for j in range(1, n):
            prev[j] = prev[j - 1] + grid[0][j]

        # process remaining rows
        for i in range(1, m):
            temp = [0] * n
            for j in range(n):
                if j == 0:
                    # can only come from top
                    temp[j] = grid[i][j] + prev[j]
                else:
                    # min of top (prev[j]) and left (temp[j-1])
                    temp[j] = grid[i][j] + min(prev[j], temp[j - 1])
            prev = temp

        return prev[n - 1]
