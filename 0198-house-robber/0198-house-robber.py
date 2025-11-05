class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # ------------------------------
        # \U0001f4a1 RECURSIVE APPROACH (TLE)
        # ------------------------------
        # Intuition:
        # - At each house, we have 2 choices: rob it and move to i+2, or skip and move to i+1.
        # - We try all combinations recursively.
        # - Exponential time due to overlapping subproblems.

        # def solve(ind):
        #     if ind >= n:
        #         return 0
        #     
        #     pick = nums[ind] + solve(ind + 2)
        #     non_pick = 0 + solve(ind + 1)
        #     return max(pick, non_pick)
        # 
        # return solve(0)

        # ----------------------------------
        # \U0001f4a1 MEMOIZATION (TOP-DOWN DP)
        # ----------------------------------
        # Intuition:
        # - Same as recursive, but we store already computed results.
        # - Time complexity reduces from O(2^n) to O(n).
        # - Space: O(n) for dp array + O(n) for recursion stack

        # dp = [-1] * n
        # def solve(ind):
        #     if ind >= n:
        #         return 0
        #     if dp[ind] != -1:
        #         return dp[ind]
        #     pick = nums[ind] + solve(ind + 2)
        #     non_pick = solve(ind + 1)
        #     dp[ind] = max(pick, non_pick)
        #     return dp[ind]
        # 
        # return solve(0)

        # --------------------------------------
        # \U0001f4a1 TABULATION (BOTTOM-UP DP)
        # --------------------------------------
        # Intuition:
        # - Convert recursion to iteration.
        # - dp[i] represents max loot from i to end.
        # - We fill dp array from the end towards 0.
        # - Time: O(n), Space: O(n)

        # if n == 0:
        #     return 0
        # if n == 1:
        #     return nums[0]
        #
        # dp = [0] * (n + 2)  # extra 2 to handle index out of bounds
        # for i in range(n - 1, -1, -1):
        #     dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
        #
        # return dp[0]

        # --------------------------------------
        # ✅ SPACE OPTIMIZATION
        # --------------------------------------
        # Intuition:
        # - We only need next and next-to-next values, not whole dp array.
        # - Use two variables instead of dp array.
        # - Time: O(n), Space: O(1)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        next1 = 0  # dp[i + 1]
        next2 = 0  # dp[i + 2]

        for i in range(n - 1, -1, -1):
            curr = max(nums[i] + next2, next1)
            next2 = next1
            next1 = curr

        return next1
