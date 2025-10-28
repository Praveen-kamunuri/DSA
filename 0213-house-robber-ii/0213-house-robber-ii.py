class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return nums[0]

        def solve_dp(start, end, dp):
            if start > end:
                return 0

            if dp[start] != -1:
                return dp[start]

            pick = nums[start] + solve_dp(start + 2, end, dp)
            not_pick = 0 + solve_dp(start + 1, end, dp)

            dp[start] = max(pick, not_pick)
            return dp[start]


        dp1 = [-1] * n
        first_pick = solve_dp(0, n - 2, dp1)

        dp2 = [-1] * n
        first_skip = solve_dp(1, n - 1, dp2)

        return max(first_pick, first_skip)
        