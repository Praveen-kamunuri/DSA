class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

       
                
        n = len(nums)

        total_sum = 0

        for i in range(n):
            total_sum += nums[i]

        if total_sum - target < 0:
            return 0

        if (total_sum - target) % 2 != 0:
            return 0

        s2  = (total_sum - target) // 2

        dp = [[0] * (s2 + 1)for _ in range(n)]

        if nums[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1

        if nums[0] != 0 and nums[0] <= s2:
            dp[0][nums[0]] = 1

        for ind in range(1, n):
            for target in range(s2 + 1):
                take = 0
                if nums[ind] <= target:
                    take = dp[ind - 1][target - nums[ind]]
                not_take = dp[ind - 1][target]

                dp[ind][target] = take + not_take

        return dp[n - 1][s2]

        