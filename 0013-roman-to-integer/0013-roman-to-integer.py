class Solution:
    def romanToInt(self, s: str) -> int:
        # Create a dictionary (hashmap) to map Roman numerals to their integer values.
        hashmap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        res = 0          # Initialize the result variable to store the integer value.
        prev_val = 0     # Initialize a variable to keep track of the previous Roman numeral value.
        
        # Iterate through the input string 's' in reverse order.
        for i in reversed(s):
            if hashmap[i] >= prev_val:
                res += hashmap[i]   # If the current value is greater or equal to the previous, add it to the result.
            else:
                res -= hashmap[i]   # If the current value is smaller than the previous, subtract it from the result.
            prev_val = hashmap[i]   # Update the previous value for the next iteration.
        
        return res   # Return the final integer result.
