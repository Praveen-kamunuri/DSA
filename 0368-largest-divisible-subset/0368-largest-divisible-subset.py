class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        sorted_nums = sorted(nums)

        n = len(sorted_nums)

        dp = [[None for _ in range(n + 1)]for _ in range(n)]

        def calLDS(ind, prev_ind, dp):

            if ind == n:
                return []
            
            if dp[ind][prev_ind + 1] != None:
                return dp[ind][prev_ind + 1]

            not_pick = calLDS(ind + 1, prev_ind, dp)

            pick = []

            if prev_ind == -1 or sorted_nums[ind] % sorted_nums[prev_ind] == 0:
                
                pick = [sorted_nums[ind]] + calLDS(ind + 1, ind, dp)
            
            dp[ind][prev_ind + 1] = max(pick, not_pick, key = len)

            return dp[ind][prev_ind + 1]
      
        return calLDS(0, -1, dp)