# ============================================================
# 188. Best Time to Buy and Sell Stock IV
#
# STATE:
# (ind, canBuy, tradesLeft)
#
# ind        -> current day
# canBuy=1   -> can buy stock
# canBuy=0   -> holding stock, can sell
# tradesLeft -> transactions remaining
#
# Transaction count decreases ONLY on SELL.
# ============================================================


# ============================================================
# 1. RECURSION
#
# Time  : O(2^N)
# Space : O(N)
# ============================================================

# class Solution:
#     def maxProfit(self, k: int, prices: List[int]) -> int:
#
#         n = len(prices)
#
#         def dfs(ind, canBuy, tradesLeft):
#
#             if ind == n or tradesLeft == 0:
#                 return 0
#
#             if canBuy:
#
#                 return max(
#                     -prices[ind] +
#                     dfs(ind + 1, 0, tradesLeft),
#
#                     dfs(ind + 1, 1, tradesLeft)
#                 )
#
#             else:
#
#                 return max(
#                     prices[ind] +
#                     dfs(ind + 1, 1, tradesLeft - 1),
#
#                     dfs(ind + 1, 0, tradesLeft)
#                 )
#
#         return dfs(0, 1, k)


# ============================================================
# 2. MEMOIZATION
#
# Time  : O(N*K)
# Space : O(N*K) + O(N)
# ============================================================

# class Solution:
#     def maxProfit(self, k: int, prices: List[int]) -> int:
#
#         n = len(prices)
#
#         dp = [[[-1 for _ in range(k + 1)]
#                for _ in range(2)]
#                for _ in range(n)]
#
#         def dfs(ind, canBuy, tradesLeft):
#
#             if ind == n or tradesLeft == 0:
#                 return 0
#
#             if dp[ind][canBuy][tradesLeft] != -1:
#                 return dp[ind][canBuy][tradesLeft]
#
#             if canBuy:
#
#                 profit = max(
#                     -prices[ind] +
#                     dfs(ind + 1, 0, tradesLeft),
#
#                     dfs(ind + 1, 1, tradesLeft)
#                 )
#
#             else:
#
#                 profit = max(
#                     prices[ind] +
#                     dfs(ind + 1, 1, tradesLeft - 1),
#
#                     dfs(ind + 1, 0, tradesLeft)
#                 )
#
#             dp[ind][canBuy][tradesLeft] = profit
#
#             return profit
#
#         return dfs(0, 1, k)


# ============================================================
# 3. TABULATION
#
# Time  : O(N*K)
# Space : O(N*K)
# ============================================================

# class Solution:
#     def maxProfit(self, k: int, prices: List[int]) -> int:
#
#         n = len(prices)
#
#         dp = [[[0 for _ in range(k + 1)]
#                for _ in range(2)]
#                for _ in range(n + 1)]
#
#         for ind in range(n - 1, -1, -1):
#
#             for canBuy in range(2):
#
#                 for tradesLeft in range(1, k + 1):
#
#                     if canBuy:
#
#                         dp[ind][canBuy][tradesLeft] = max(
#                             -prices[ind] +
#                             dp[ind + 1][0][tradesLeft],
#
#                             dp[ind + 1][1][tradesLeft]
#                         )
#
#                     else:
#
#                         dp[ind][canBuy][tradesLeft] = max(
#                             prices[ind] +
#                             dp[ind + 1][1][tradesLeft - 1],
#
#                             dp[ind + 1][0][tradesLeft]
#                         )
#
#         return dp[0][1][k]


# ============================================================
# 4. SPACE OPTIMIZATION (SUBMIT THIS)
#
# Time  : O(N*K)
# Space : O(K)
# ============================================================

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        n = len(prices)

        ahead = [[0 for _ in range(k + 1)]
                 for _ in range(2)]

        for ind in range(n - 1, -1, -1):

            curr = [[0 for _ in range(k + 1)]
                    for _ in range(2)]

            for canBuy in range(2):

                for tradesLeft in range(1, k + 1):

                    if canBuy:

                        curr[canBuy][tradesLeft] = max(
                            -prices[ind] +
                            ahead[0][tradesLeft],

                            ahead[1][tradesLeft]
                        )

                    else:

                        curr[canBuy][tradesLeft] = max(
                            prices[ind] +
                            ahead[1][tradesLeft - 1],

                            ahead[0][tradesLeft]
                        )

            ahead = curr

        return ahead[1][k]