class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        n = len(nums)

        total_sum = 0

        for i in range(n):
            total_sum += nums[i]
        
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2

        dp = [[-1] * (target + 1) for _ in range(n)]

        def find_equal_subset_sum(ind, target, dp):

            if target == 0:
                return True

            if ind == 0:
                return False

            if dp[ind][target] != -1:
                return dp[ind][target]

            take = False

            if nums[ind] <= target:
                take = find_equal_subset_sum(ind - 1, target - nums[ind], dp)
            
            not_take = find_equal_subset_sum(ind - 1, target, dp)

            dp[ind][target] = take or not_take

            return dp[ind][target]

        return find_equal_subset_sum(n - 1, target, dp)

