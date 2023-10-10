class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0  # Initialize the result to 1.0
        nn = n  # Create a variable nn to work with n (to handle negative n)
        
        # If n is negative, make it positive to simplify calculations
        if nn < 0:
            nn = -1 * nn

        # Loop while nn is greater than 0
        while nn > 0:
            # If nn is even, square x and halve nn
            if nn % 2 == 0:
                x = x * x
                nn = nn // 2
            else:
                # If nn is odd, multiply ans by x and subtract 1 from nn
                ans = ans * x
                nn = nn - 1
        
        # If the original n was negative, take the reciprocal of ans
        if n < 0:
            ans = 1.0 / ans
        
        return ans  # Return the final result
