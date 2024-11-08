class Solution:
    def reverse(self, x: int) -> int:
        
        # Initialize sign as positive (+1)
        sign = 1
        
        # Check if the number is negative
        if x < 0:
            # Change sign to negative if x is negative
            sign = -1
            # Make x positive for easier manipulation
            x = abs(x)
        
        # Variable to store the reversed number
        c = 0
        
        # Loop until x becomes zero
        while x > 0:
            # Get the last digit of x
            rem = x % 10
            # Append it to the reversed number by shifting digits
            c = c * 10 + rem
            # Remove the last digit from x
            x = x // 10
            
        # Multiply by sign to restore the original sign
        res = c * sign
        
        # Check if the result is within the 32-bit signed integer range
        if -2 ** 31 <= res <= (2 ** 31) - 1:
            return res
        else:
            # Return 0 if the result overflows
            return 0
