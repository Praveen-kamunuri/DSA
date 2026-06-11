class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)

        dp = [[0 for _ in range(n + 1)]for _ in range(n + 1)]

        for ind in range(n - 1, -1, -1):
            for prev_ind in range(ind - 1, -2, -1):

                not_pick = 0 + dp[ind + 1][prev_ind + 1]

                pick = 0

                if prev_ind == -1 or nums[prev_ind] < nums[ind]:
                    pick = 1 + dp[ind + 1][ind + 1]
                
                dp[ind][prev_ind + 1] = max(pick, not_pick)

        return dp[0][0]