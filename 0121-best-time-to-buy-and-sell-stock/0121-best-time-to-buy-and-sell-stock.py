class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Get the number of days (the length of the prices list)
        n = len(prices)
        
        # Initialize the profit to 0 and the minimum price to the price on the first day
        profit = 0
        mini = prices[0]
        
        # Loop through the prices starting from the second day (index 1)
        for i in range(1, n):
            # Calculate the profit (current price - minimum price so far)
            cost = prices[i] - mini
            
            # Update the maximum profit if the current profit is greater
            profit = max(profit, cost)
            
            # Update the minimum price if the current price is lower
            mini = min(mini, prices[i])
        
        # Return the maximum profit achievable
        return profit
