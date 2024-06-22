class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for the 32-bit integer limits
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        # Edge case: divisor is 0 (though it's assumed this won't be the input)
        if divisor == 0:
            raise ValueError("Divisor cannot be zero")

        # Edge case: dividend is 0
        if dividend == 0:
            return 0

        # Edge case: overflow handling
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive values for simplicity
        dividend, divisor = abs(dividend), abs(divisor)

        # Division using bit manipulation
        quotient = 0
        # Find the largest multiple
        most_significant_bit = 0
        while dividend >= (divisor << most_significant_bit):
            most_significant_bit += 1

        # Perform the subtraction
        for bit in range(most_significant_bit - 1, -1, -1):
            if dividend >= (divisor << bit):
                dividend -= (divisor << bit)
                quotient += (1 << bit)

        # Apply the sign
        if negative:
            quotient = -quotient

        # Clamp the result to the 32-bit signed integer range
        return max(MIN_INT, min(MAX_INT, quotient))
