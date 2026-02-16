class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        n = len(nums)

        total_sum = 0

        for i in range(n):
            total_sum += nums[i]
        
        if total_sum % 2 != 0:
            return False
        
        target_sum = total_sum // 2

        dp = [[False] * (target_sum + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = True
        
        if nums[0] <= target_sum:
            dp[0][nums[0]] = True
        
        for ind in range(1, n):
            for target in range(1, target_sum + 1):
                take = False
                if nums[ind] <= target:
                    take = dp[ind - 1][target - nums[ind]]
                not_take = dp[ind - 1][target]

                dp[ind][target] = take or not_take
        
        return dp[n - 1][target_sum]

        