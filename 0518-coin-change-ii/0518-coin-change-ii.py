class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        """
        PROBLEM TYPE
        Unbounded Knapsack / Coin Change (Count combinations)

        We can take a coin unlimited times.

        Recurrence idea:
        take     -> stay at same index (reuse coin)
        not_take -> move to previous index
        """

        n = len(coins)

        # ============================================================
        # 1️⃣ PURE RECURSION
        # TC → Exponential
        # SC → O(amount) recursion stack
        # ============================================================

        """
        def solve(ind, target):

            # base case
            if ind == 0:
                if target % coins[0] == 0:
                    return 1
                return 0

            take = 0
            if coins[ind] <= target:
                take = solve(ind, target - coins[ind])  # same index (unbounded)

            not_take = solve(ind-1, target)

            return take + not_take
        """

        # ============================================================
        # 2️⃣ MEMOIZATION (Top Down DP)
        # TC → O(N * amount)
        # SC → O(N * amount) dp + recursion stack
        # ============================================================

        """
        dp = [[-1]*(amount+1) for _ in range(n)]

        def solve(ind, target):

            if ind == 0:
                if target % coins[0] == 0:
                    return 1
                return 0

            if dp[ind][target] != -1:
                return dp[ind][target]

            take = 0
            if coins[ind] <= target:
                take = solve(ind, target - coins[ind])

            not_take = solve(ind-1, target)

            dp[ind][target] = take + not_take
            return dp[ind][target]

        return solve(n-1, amount)
        """

        # ============================================================
        # 3️⃣ TABULATION
        # TC → O(N * amount)
        # SC → O(N * amount)
        # ============================================================

        """
        dp = [[0]*(amount+1) for _ in range(n)]

        # base row
        for t in range(amount+1):
            if t % coins[0] == 0:
                dp[0][t] = 1

        for ind in range(1, n):
            for t in range(amount+1):

                not_take = dp[ind-1][t]

                take = 0
                if coins[ind] <= t:
                    take = dp[ind][t-coins[ind]]

                dp[ind][t] = take + not_take

        return dp[n-1][amount]
        """

        # ============================================================
        # 4️⃣ SPACE OPTIMIZATION (FINAL RUNNING CODE)
        # TC → O(N * amount)
        # SC → O(amount)
        # ============================================================

        """
        INTUITION

        In tabulation we only use:
        dp[ind]
        dp[ind-1]

        So we can compress the 2D DP into 1D.

        Key idea:
        For unbounded problems we iterate target LEFT → RIGHT
        so that same row values can be reused.
        """

        dp = [0] * (amount + 1)

        # base case
        for t in range(amount + 1):
            if t % coins[0] == 0:
                dp[t] = 1

        for ind in range(1, n):
            for t in range(amount + 1):

                take = 0
                if coins[ind] <= t:
                    take = dp[t - coins[ind]]

                not_take = dp[t]

                dp[t] = take + not_take

        return dp[amount]