class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        n = len(prices)

        # dp = [[[-1]for _ in range(k + 1)]for _ in range(2)for _ in range(n)]

        dp = [[[-1 for _ in range(k + 1)]for _ in range(2)]for _ in range(n)]

        def calProfit(ind, canBuy, totalTrades, prices, n, k):

            if ind == n or totalTrades == 0:
                return 0

            if dp[ind][canBuy][totalTrades] != -1:
                return dp[ind][canBuy][totalTrades]

            if canBuy == 1:
                profit = max(
                    -prices[ind] + calProfit(ind + 1, 0, totalTrades, prices, n, k),
                    0 + calProfit(ind + 1, 1, totalTrades, prices, n, k)
                )

                dp[ind][canBuy][totalTrades] = profit
                return profit

            else:
                profit = max(
                    prices[ind] + calProfit(ind + 1, 1, totalTrades - 1, prices, n, k),
                    0 + calProfit(ind + 1, 0, totalTrades, prices, n, k)
                )

                dp[ind][canBuy][totalTrades] = profit
                return profit
        
        return calProfit(0, 1, k, prices, n, k)


        