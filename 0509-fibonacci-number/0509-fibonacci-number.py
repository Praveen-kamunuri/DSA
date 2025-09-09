class Solution:
    # ----------------------------- #
    # 1. Memoization (Top-Down DP)  #
    # ----------------------------- #
    # Intuition:
    # - Use recursion + cache results to avoid repeated calls.
    # - F(n) = F(n-1) + F(n-2), store computed values in a dictionary/array.
    #
    # Approach:
    # - Base cases: F(0)=0, F(1)=1
    # - Recursively compute F(n) and memoize results.
    #
    # Time Complexity: O(n)  -> Each state solved once.
    # Space Complexity: O(n) -> Recursion stack + memo array.
    #
    # def fib(self, n: int) -> int:
    #     dp = [-1] * (n + 1)
    #
    #     def solve(k):
    #         if k <= 1:
    #             return k
    #         if dp[k] != -1:
    #             return dp[k]
    #         dp[k] = solve(k - 1) + solve(k - 2)
    #         return dp[k]
    #
    #     return solve(n)


    # ----------------------------- #
    # 2. Tabulation (Bottom-Up DP)  #
    # ----------------------------- #
    # Intuition:
    # - Build solutions iteratively from the bottom.
    # - Start from base cases (0,1) and fill DP array until n.
    #
    # Approach:
    # - dp[0]=0, dp[1]=1
    # - dp[i] = dp[i-1] + dp[i-2]
    #
    # Time Complexity: O(n)
    # Space Complexity: O(n) -> Extra DP array
    #
    # def fib(self, n: int) -> int:
    #     if n == 0:
    #         return 0
    #     dp = [-1] * (n + 1)
    #     dp[0], dp[1] = 0, 1
    #
    #     for i in range(2, n + 1):
    #         dp[i] = dp[i - 1] + dp[i - 2]
    #
    #     return dp[n]


    # ----------------------------- #
    # 3. Space Optimized DP         #
    # ----------------------------- #
    # Intuition:
    # - We don’t need the whole DP array, only last two values at any time.
    # - Keep track of prev1 and prev2 instead of full array.
    #
    # Approach:
    # - Base cases: if n==0 return 0, if n==1 return 1
    # - Iteratively compute using only two variables.
    #
    # Time Complexity: O(n)
    # Space Complexity: O(1) -> Only two variables used
    #
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        prev2, prev1 = 0, 1  # F(0), F(1)

        for i in range(2, n + 1):
            curr = prev1 + prev2
            prev2, prev1 = prev1, curr

        return prev1
