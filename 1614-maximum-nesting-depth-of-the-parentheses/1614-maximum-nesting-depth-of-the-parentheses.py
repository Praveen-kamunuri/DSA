class Solution:
    def maxDepth(self, s: str) -> int:
        # If the input string is empty, the maximum depth is 0.
        if s == "":
            return 0
        
        curr_max = 0  # Initialize a variable to keep track of the current depth.
        maxi = 0      # Initialize a variable to store the maximum depth found.

        # Iterate through each character in the input string.
        for i in s:
            if i == "(":
                curr_max += 1  # Increment the current depth for an open parenthesis '('.
            elif i == ")":
                maxi = max(curr_max, maxi)  # Update the maximum depth if needed.
                curr_max -= 1  # Decrement the current depth for a closing parenthesis ')'.
            else:
                continue  # Ignore any other characters.

        return maxi  # Return the maximum depth found.
