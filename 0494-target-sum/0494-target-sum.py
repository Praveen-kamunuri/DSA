class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def count_partitions(ind, target, dp, arr):

            if ind == 0:
                if target == 0 and arr[0] == 0:
                    return 2
                if target == 0 or arr[0] == target:
                    return 1
                return 0

            if dp[ind][target] != -1:
                return dp[ind][target]

            take = 0
            if arr[ind] <= target:
                take = count_partitions(ind - 1, target - arr[ind], dp, arr)
            not_take = count_partitions(ind - 1, target, dp, arr)

            dp[ind][target] = take + not_take
            return dp[ind][target]

                
        n = len(nums)

        total_sum = 0

        for i in range(n):
            total_sum += nums[i]

        if total_sum - target < 0:
            return 0

        if (total_sum - target) % 2 != 0:
            return 0

        s2  = (total_sum - target) // 2

        dp = [[-1] * (s2 + 1)for _ in range(n)]

        res = count_partitions(n - 1, s2, dp, nums)

        return res
        