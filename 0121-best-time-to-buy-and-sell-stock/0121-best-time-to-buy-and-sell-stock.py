class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        min_price = prices[0]  # Initialize min_price with the first price

        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])  # Update min_price if necessary
            max_profit = max(max_profit, prices[i] - min_price)  # Update max_profit

        return max_profit
