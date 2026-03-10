class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)

        dp = [[0] * (amount + 1)for _ in range(n)]

        for t in range(amount + 1):
            if t % coins[0] == 0:
                dp[0][t] = 1

        for ind in range(1, n):
            for target in range(amount + 1):
                take = 0
                if coins[ind] <= target:
                    take = dp[ind][target - coins[ind]]
                not_take = dp[ind - 1][target]

                dp[ind][target] = take + not_take
        
        return dp[n - 1][amount]