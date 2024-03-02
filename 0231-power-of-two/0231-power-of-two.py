class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Check if n is less than or equal to 0
        if n <= 0:
            return False  # If so, n cannot be a power of two, return False
        
        # Check if n is a power of two using bitwise AND with n-1
        # A power of two has only one bit set, so n & (n-1) will be 0
        return n & (n-1) == 0  # Return True if n is a power of two, False otherwise
