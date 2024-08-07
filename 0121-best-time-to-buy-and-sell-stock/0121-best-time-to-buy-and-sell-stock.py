from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)  # Length of the prices list

        mini = prices[0]  # Initialize the minimum price to the first price

        profit = 0  # Initialize the maximum profit to 0

        for i in range(1, n):
            cost = prices[i] - mini  # Calculate potential profit if selling at prices[i]

            profit = max(profit, cost)  # Update maximum profit if the current cost is higher

            mini = min(prices[i], mini)  # Update minimum price to the lower of current price or previous minimum

        return profit  # Return the maximum profit found

        # Time Complexity: O(n)
        # We iterate through the list once, performing constant time operations within the loop.
        # Space Complexity: O(1)
        # We use a fixed amount of extra space (variables `mini` and `profit`), regardless of the input size.
