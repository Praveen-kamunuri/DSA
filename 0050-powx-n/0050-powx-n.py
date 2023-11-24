class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Initialize the result to 1.0
        ans = 1.0
        
        # Make a copy of n (nn) to handle negative exponents
        nn = n
        
        # If the exponent is negative, make it positive
        if nn < 0:
            nn = -1 * nn
        
        # Iterate through the bits of the exponent
        while nn:
            # If the current bit is 1, multiply ans by x
            if nn % 2:
                ans = ans * x
                nn = nn - 1
            # Square x and halve the exponent
            else:
                x = x * x
                nn = nn // 2
        
        # If the original exponent was negative, take the reciprocal of ans
        if n < 0:
            ans = 1.0 / ans
        
        # Return the final result
        return ans
