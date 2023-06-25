class Solution(object):
    def fib(self, n):
        # Base cases: if n is 0 or 1, return n
        if n <= 1:
            return n
        else:
            # Recursive calls to calculate Fibonacci numbers
            last = self.fib(n-1)
            slast = self.fib(n-2)
        # Return the sum of the last two Fibonacci numbers
        return last + slast
