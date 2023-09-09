class Solution(object):
    def combinationSum4(self, nums, target):
         # Initialize an array to store the number of combinations for each target value
        dp = [0] * (target + 1)

        # There's one way to reach target value 0, which is by not selecting any number
        dp[0] = 1

        # Calculate the number of combinations for each target value from 1 to target
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]

        return dp[target]

        
        