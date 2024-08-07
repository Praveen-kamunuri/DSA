class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        
        mini = prices[0]
        
        profit = 0
        
        for i  in range(1, n):
            cost = prices[i] - mini
            
            profit = max(profit, cost)
            
            mini = min(prices[i], mini)
            
        return profit
        