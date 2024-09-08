class StockSpanner:
    def __init__(self):
        # Initialize an empty stack to store pairs of (price, span).
        self.stack = []
        
    def next(self, price: int) -> int:
        # Initialize the span for the current price to 1 (itself).
        span = 1
        
        # While the stack is not empty and the price on the top of the stack is less than or equal to the current price
        while self.stack and price >= self.stack[-1][0]:
            # Add the span of the price on top of the stack to the current span
            span += self.stack.pop()[1]
        
        # Push the current price and its span onto the stack
        self.stack.append((price, span))
        
        # Return the computed span for the current price
        return span

# Time Complexity:
# Each price is pushed and popped from the stack at most once. Therefore, the time complexity for each call to next() is O(1).

# Space Complexity:
# In the worst case, all prices are stored in the stack. Therefore, the space complexity is O(n), where n is the number of calls to next().
