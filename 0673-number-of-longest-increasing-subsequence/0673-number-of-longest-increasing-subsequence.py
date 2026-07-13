class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        n = len(nums)

        dp = [1] * n

        cnt = [1] * n

        maxi = 1

        for i in range(n):
            for j in range(i):

                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1

                    cnt[i] = cnt[j]

                elif nums[j] < nums[i] and dp[j] + 1 == dp[i]:

                    cnt[i] += cnt[j]

            print(maxi, dp[i])
            maxi = max(maxi, dp[i])

        print(maxi)
        res = 0
        for i in range(n):
            if dp[i] == maxi:
                res += cnt[i]

        return res

