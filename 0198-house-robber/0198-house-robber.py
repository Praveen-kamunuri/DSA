class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        dp = [0] * n
        dp[0] = nums[0]

        for ind in range(1, n):
            take = nums[ind]
            if ind > 1:
                take += dp[ind - 2]
            not_take = 0 + dp[ind - 1]

            dp[ind] = max(take, not_take)
        return dp[n - 1]

        