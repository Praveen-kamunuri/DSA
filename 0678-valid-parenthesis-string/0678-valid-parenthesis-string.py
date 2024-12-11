class Solution:
    def checkValidString(self, s: str) -> bool:
        # Initialize mini and maxi to track the minimum and maximum number 
        # of open parentheses that could be valid at any point in the string.
        mini = 0
        maxi = 0

        # Iterate through each character in the string
        for i in s:
            if i == '(':  # If the character is an open parenthesis
                mini += 1  # Increment mini as this must be balanced later
                maxi += 1  # Increment maxi as it's a possible valid open parenthesis
            elif i == ')':  # If the character is a close parenthesis
                mini -= 1  # Decrement mini as this balances an open parenthesis
                maxi -= 1  # Decrement maxi for the same reason
            else:  # If the character is '*'
                mini -= 1  # Assume '*' acts as a ')'
                maxi += 1  # Assume '*' acts as a '('

            # If mini goes below 0, reset it to 0 because '*' can also act as an empty string
            if mini < 0:
                mini = 0

            # If maxi goes below 0, it means there are more ')' than possible '('
            # This invalidates the string immediately
            if maxi < 0:
                return False

        # If mini is 0, it means all open parentheses are balanced
        return mini == 0

# Time Complexity (TC): O(n)
# The solution iterates through the string once, performing constant-time operations for each character.

# Space Complexity (SC): O(1)
# The algorithm uses a constant amount of additional space regardless of the input size.
