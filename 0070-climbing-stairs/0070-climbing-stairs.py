class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Intuition:
        - To reach step 'n', you can come either from:
            1. step (n-1) by taking 1 step
            2. step (n-2) by taking 2 steps
        - So total ways to reach step 'n' = ways(n-1) + ways(n-2).
        - This is exactly like the Fibonacci sequence.
        - We use DP to avoid recomputation.

        Approaches:
        1. Recursion (Exponential time, memory exceeded)
        2. Memoization (Top-Down DP with caching)
        3. Tabulation (Bottom-Up DP using an array)
        4. Space Optimization (Only keep last 2 states → O(1) space)
        """

        # --------------------
        # 1. Recursion (TLE ❌)
        # def solve(i):
        #     if i <= 1:
        #         return 1
        #     return solve(i - 1) + solve(i - 2)
        # return solve(n)

        # --------------------
        # 2. Memoization (Top-Down ✅)
        # dp = [-1] * (n + 1)
        # def solve(i):
        #     if i <= 1:
        #         return 1
        #     if dp[i] != -1:
        #         return dp[i]
        #     dp[i] = solve(i - 1) + solve(i - 2)
        #     return dp[i]
        # return solve(n)

        # --------------------
        # 3. Tabulation (Bottom-Up ✅)
        # dp = [-1] * (n + 1)
        # dp[0] = 1
        # dp[1] = 1
        # for i in range(2, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[n]

        # --------------------
        # 4. Space Optimization (Final Answer ✅)
        prev1 = 1
        prev2 = 1
        for i in range(2, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        return prev1
