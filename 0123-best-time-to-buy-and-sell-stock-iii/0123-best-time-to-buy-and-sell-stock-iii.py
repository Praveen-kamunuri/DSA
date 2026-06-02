class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        # ============================================================
        # APPROACH 1 : RECURSION
        # ============================================================
        #
        # State:
        # ind         -> current day
        # canBuy      -> 1 means we can buy, 0 means we must sell
        # totalTrades -> transactions remaining
        #
        # Choices:
        #
        # If canBuy:
        #   Buy     -> -prices[ind] + next state
        #   Not Buy -> move to next day
        #
        # If cannot buy:
        #   Sell      -> +prices[ind] + next state
        #   Not Sell  -> move to next day
        #
        # Base Case:
        #   No days left
        #   OR
        #   No transactions left
        #
        # Time  : O(2^N)
        # Space : O(N) recursion stack
        #
        # def calProfit(ind, canBuy, totalTrades):
        #
        #     if ind == n or totalTrades == 0:
        #         return 0
        #
        #     if canBuy:
        #         return max(
        #             -prices[ind] + calProfit(ind + 1, 0, totalTrades),
        #             calProfit(ind + 1, 1, totalTrades)
        #         )
        #
        #     return max(
        #         prices[ind] + calProfit(ind + 1, 1, totalTrades - 1),
        #         calProfit(ind + 1, 0, totalTrades)
        #     )
        #
        # return calProfit(0, 1, 2)



        # ============================================================
        # APPROACH 2 : MEMOIZATION
        # ============================================================
        #
        # Observation:
        # Same states are being recomputed.
        #
        # State dimensions:
        #   ind         -> n
        #   canBuy      -> 2
        #   totalTrades -> 3 (0,1,2)
        #
        # dp[ind][canBuy][totalTrades]
        #
        # Time  : O(N * 2 * 3)
        # Space : O(N * 2 * 3) + O(N)
        #
        # dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]
        #
        # def calProfit(ind, canBuy, totalTrades):
        #
        #     if ind == n or totalTrades == 0:
        #         return 0
        #
        #     if dp[ind][canBuy][totalTrades] != -1:
        #         return dp[ind][canBuy][totalTrades]
        #
        #     if canBuy:
        #         profit = max(
        #             -prices[ind] + calProfit(ind + 1, 0, totalTrades),
        #             calProfit(ind + 1, 1, totalTrades)
        #         )
        #     else:
        #         profit = max(
        #             prices[ind] + calProfit(ind + 1, 1, totalTrades - 1),
        #             calProfit(ind + 1, 0, totalTrades)
        #         )
        #
        #     dp[ind][canBuy][totalTrades] = profit
        #
        #     return profit
        #
        # return calProfit(0, 1, 2)



        # ============================================================
        # APPROACH 3 : TABULATION
        # ============================================================
        #
        # Convert recursion into bottom-up DP.
        #
        # Base Cases:
        # dp[n][*][*] = 0
        # dp[*][*][0] = 0
        #
        # Fill from back:
        # day n-1 -> day 0
        #
        # Time  : O(N * 2 * 3)
        # Space : O(N * 2 * 3)
        #
        # dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]
        #
        # for ind in range(n - 1, -1, -1):
        #
        #     for canBuy in range(2):
        #
        #         for totalTrades in range(1, 3):
        #
        #             if canBuy:
        #
        #                 dp[ind][canBuy][totalTrades] = max(
        #                     -prices[ind] + dp[ind + 1][0][totalTrades],
        #                     dp[ind + 1][1][totalTrades]
        #                 )
        #
        #             else:
        #
        #                 dp[ind][canBuy][totalTrades] = max(
        #                     prices[ind] + dp[ind + 1][1][totalTrades - 1],
        #                     dp[ind + 1][0][totalTrades]
        #                 )
        #
        # return dp[0][1][2]



        # ============================================================
        # APPROACH 4 : SPACE OPTIMIZATION
        # ============================================================
        #
        # Observe:
        # dp[ind] depends only on dp[ind+1]
        #
        # Therefore we only need:
        #
        # ahead -> represents dp[ind+1]
        # curr  -> represents dp[ind]
        #
        # Time  : O(N * 2 * 3)
        # Space : O(2 * 3)
        #
        ahead = [[0 for _ in range(3)] for _ in range(2)]

        for ind in range(n - 1, -1, -1):

            curr = [[0 for _ in range(3)] for _ in range(2)]

            for canBuy in range(2):

                for totalTrades in range(1, 3):

                    if canBuy:

                        curr[canBuy][totalTrades] = max(
                            -prices[ind] + ahead[0][totalTrades],
                            ahead[1][totalTrades]
                        )

                    else:

                        curr[canBuy][totalTrades] = max(
                            prices[ind] + ahead[1][totalTrades - 1],
                            ahead[0][totalTrades]
                        )

            ahead = curr

        return ahead[1][2]