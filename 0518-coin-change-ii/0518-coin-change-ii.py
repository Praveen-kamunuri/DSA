class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        def count_comb(ind, target, arr, dp):
            if ind == 0:
                if target % arr[0] == 0:
                    return 1
                return 0

            if dp[ind][target] != -1:
                return dp[ind][target]

            take = 0
            if arr[ind] <= target:
                take = count_comb(ind, target - arr[ind], arr, dp)             
            
            not_take = count_comb(ind - 1, target, arr, dp)

            dp[ind][target] = take + not_take

            return dp[ind][target]
            
        n = len(coins)

        dp = [[-1] * (amount + 1)for _ in range(n)]


        res = count_comb(n - 1, amount, coins, dp)
        return res