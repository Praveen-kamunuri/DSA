class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        dp = [[-1 for _ in range(2)]for _ in range(n)]

        def calProfit(ind, canBuy, n, dp):
            if ind == n:
                return 0

            if dp[ind][canBuy] != -1:
                return dp[ind][canBuy]
            

            
            if canBuy == 1:
                profit = max(
                    -prices[ind] + calProfit(ind + 1, 0, n, dp), 
                
                    0 + calProfit(ind + 1, 1, n, dp)
                )
                dp[ind][canBuy] = profit


            else:
                profit = max(
                    prices[ind] + calProfit(ind + 1, 1, n, dp),

                    0 + calProfit(ind + 1, 0, n, dp)

                )
                dp[ind][canBuy] = profit

            return dp[ind][canBuy]

        return calProfit(0, 1, n, dp)
        