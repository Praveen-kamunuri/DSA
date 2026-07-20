# 🏠 HOUSE ROBBER II (CIRCULAR HOUSES)
# You cannot rob both first and last houses.

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        # -------------------------------------------------------
        # 🧩 1️⃣ RECURSION (Brute Force)
        # Intuition:
        # - For each house i, choose to "take" or "skip".
        # - If you take, add current value + solve for i-2.
        # - If you skip, solve for i-1.
        # -------------------------------------------------------
        # def rob_linear_rec(i, arr):
        #     if i == 0:
        #         return arr[0]
        #     if i < 0:
        #         return 0
        #     take = arr[i] + rob_linear_rec(i - 2, arr)
        #     not_take = rob_linear_rec(i - 1, arr)
        #     return max(take, not_take)
        #
        # TC: O(2^n)
        # SC: O(n) recursion stack

        # -------------------------------------------------------
        # 🧩 2️⃣ MEMOIZATION (Top-Down DP)
        # Intuition:
        # - Store already computed results to avoid recomputation.
        # -------------------------------------------------------
        # def rob_linear_memo(i, arr, dp):
        #     if i == 0:
        #         return arr[0]
        #     if i < 0:
        #         return 0
        #     if dp[i] != -1:
        #         return dp[i]
        #     take = arr[i] + rob_linear_memo(i - 2, arr, dp)
        #     not_take = rob_linear_memo(i - 1, arr, dp)
        #     dp[i] = max(take, not_take)
        #     return dp[i]
        #
        # TC: O(n)
        # SC: O(n) (recursion + dp)

        # -------------------------------------------------------
        # 🧩 3️⃣ TABULATION (Bottom-Up DP)
        # Intuition:
        # - Build dp[] array iteratively.
        # - dp[i] = max(arr[i] + dp[i-2], dp[i-1])
        # -------------------------------------------------------
        # def rob_linear_tab(arr):
        #     n = len(arr)
        #     dp = [0] * n
        #     dp[0] = arr[0]
        #
        #     for i in range(1, n):
        #         take = arr[i]
        #         if i > 1:
        #             take += dp[i - 2]
        #         not_take = dp[i - 1]
        #         dp[i] = max(take, not_take)
        #
        #     return dp[-1]
        #
        # TC: O(n)
        # SC: O(n)

        # -------------------------------------------------------
        # 🧩 4️⃣ SPACE OPTIMIZATION ✅ (Final)
        # Intuition:
        # - We only need dp[i-1] and dp[i-2], so store two variables.
        # -------------------------------------------------------
        def rob_linear_space_opt(arr):
            prev = arr[0]  # dp[i-1]
            prev2 = 0      # dp[i-2]

            for i in range(1, len(arr)):
                take = arr[i]
                if i > 1:
                    take += prev2
                not_take = prev
                curr = max(take, not_take)
                prev2 = prev
                prev = curr

            return prev

        # since houses are circular, exclude first or last
        first = rob_linear_space_opt(nums[:-1])  # exclude last
        second = rob_linear_space_opt(nums[1:])  # exclude first

        return max(first, second)

# -------------------------------------------------------
# ✅ Final Approach Used: Space Optimized DP
# TC: O(n)
# SC: O(1)
# -------------------------------------------------------
