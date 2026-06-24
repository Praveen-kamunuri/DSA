class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        sorted_nums = sorted(nums)

        n = len(sorted_nums)

        dp = [[[] for _ in range(n + 1)]for _ in range(n + 1)]


        for ind in range(n - 1, -1 , -1):
            for prev_ind in range(ind - 1, -2, -1):

                not_pick = dp[ind + 1][prev_ind + 1]

                pick = []

                if prev_ind == -1 or sorted_nums[ind] % sorted_nums[prev_ind] == 0:
                    pick = [sorted_nums[ind]] + dp[ind + 1][ind + 1]
                
                dp[ind][prev_ind + 1] = max(pick, not_pick, key = len)

        return dp[0][0]