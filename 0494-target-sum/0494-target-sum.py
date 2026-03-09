class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:


        def count_ways(ind, target, dp):

            if ind == 0:
                if target == 0 and nums[ind] == 0:
                    return 2
                if target == nums[0] or target == -(nums[0]):
                    return 1
                return 0
            
            if dp[ind][target] != -1:
                return dp[ind][target]
        
            take_pos = count_ways(ind - 1, target - (nums[ind]), dp)
            take_neg = count_ways(ind - 1, target + (nums[ind]), dp)

            dp[ind][target] = take_pos + take_neg

            return dp[ind][target]

        n = len(nums)

        if n == 1:

            if nums[0] == 0:
                return 2

            if nums[0] == target or nums[0] == -(target):
                return 1
           
            else:
                return 0
        
        dp = [[-1] * (target + 1)]
        res = count_ways(n - 1, target, dp)
        return res
        