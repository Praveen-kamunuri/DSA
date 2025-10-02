class Solution:
    def rob(self, nums: List[int]) -> int:


        n = len(nums)

        dp = [-1] * n

        dp[0] = 0

        def solve(ind, nums):

            if ind < 0:
                return 0
            
            if ind == 0:
                return nums[ind]

            if dp[ind] != -1:
                return dp[ind]

            pick = nums[ind] + solve(ind - 2, nums)

            non_pick = 0 + solve(ind - 1, nums)

            dp[ind] = max(pick, non_pick)

            return dp[ind]

        return solve(n - 1, nums)