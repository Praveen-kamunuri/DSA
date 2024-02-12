class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle negative exponent by converting it to positive
        nn = n
        ans = 1.0
        if nn < 0:
            nn = -1 * nn
        
        # Binary exponentiation algorithm
        while nn > 0:  
            if nn % 2 == 1:  # If the exponent is odd
                ans = ans * x
                nn = nn - 1  # Reduce the exponent by 1

            else:  # If the exponent is even
                x = x * x
                nn = nn / 2  # Halve the exponent
        
        # If the original exponent was negative, take the reciprocal of the result
        if n < 0:
            ans = 1.0 / ans
            
        return ans
