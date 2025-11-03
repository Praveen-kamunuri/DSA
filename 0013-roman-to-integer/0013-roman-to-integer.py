class Solution:
    def romanToInt(self, s: str) -> int:
        # Create a dictionary to map Roman numeral characters to their integer values
        hashmap = {
                    'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000
            }

        # Initialize variables
        res = 0  # The result will be stored here..
        pre_val = 0  # Keep track of the previous Roman numeral value
        n = len(s)  # Get the length of the input string.

        # Iterate through the Roman numeral characters in reverse order
        for i in range(n - 1, -1, -1):
            # Check if the current character's value is greater than or equal to the previous value.
            if hashmap[s[i]] >= pre_val:
                res += hashmap[s[i]]
            else:
                res -= hashmap[s[i]]
            pre_val = hashmap[s[i]]  # Update the previous value

        # Return the final result as the integer equivalent of the input Roman numeral.
        return res