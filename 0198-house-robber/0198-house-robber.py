class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        dp = [-1] * n

        def solve_dp(ind, dp, n):
            if ind >= n:
                return 0
            
            if dp[ind] != -1:
                return dp[ind]

            take = nums[ind] + solve_dp(ind + 2, dp, n)
            not_take = 0 + solve_dp(ind + 1, dp, n)

            dp[ind] = max(take, not_take)
            return dp[ind]

        solve_dp(0, dp, n)
        return dp[0]
        