class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]

        def calProfit(ind, canBuy, totalTrades, n, prices, dp):
            if ind == n or totalTrades == 0:
                return 0
            
            if dp[ind][canBuy][totalTrades] != -1:
                return dp[ind][canBuy][totalTrades]

            profit = 0

            if canBuy == 1:
                profit = max(
                    -prices[ind] + calProfit(ind + 1, 0, totalTrades, n, prices, dp),
                    0 + calProfit(ind + 1, 1, totalTrades, n, prices, dp)
                )
            
            else:
                profit = max(
                    prices[ind] + calProfit(ind + 1, 1, totalTrades - 1, n, prices, dp),
                    0 + calProfit(ind + 1, 0, totalTrades, n, prices, dp)
                )
            
            dp[ind][canBuy][totalTrades] = profit

            return dp[ind][canBuy][totalTrades]

        return calProfit(0, 1, 2, n, prices, dp)


        