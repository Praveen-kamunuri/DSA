class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return nums[0]

        def solve_tabulation(arr):
            m = len(arr)

            dp = [-1] * m
            dp[0] = arr[0]

            for i in range(1, m):
                take = arr[i] 
                if i > 1:
                    take += dp[i - 2]
                not_take = 0 + dp[i - 1]

                dp[i] = max(take, not_take)
            return dp[-1]

        first_take = solve_tabulation(nums[:-1])
        last_take = solve_tabulation(nums[1:])

        return max(first_take, last_take)
        