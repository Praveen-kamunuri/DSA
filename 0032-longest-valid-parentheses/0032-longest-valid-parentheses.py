class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Initialize stack with -1 to handle base case for valid substring calculation
        stack = [-1]

        # Variable to keep track of the maximum valid length found
        max_len = 0

        # Length of the input string
        n = len(s)

        # Iterate over each character in the string
        for i in range(n):
            if s[i] == '(':
                # Push index of '(' onto stack
                stack.append(i)
            else:
                # Pop the last index (ideally of a matching '(')
                stack.pop()

                if not stack:
                    # If stack is empty, push current index as new base
                    stack.append(i)
                else:
                    # Update max_len with the length of current valid substring
                    max_len = max(max_len, i - stack[-1])

        return max_len

# Time Complexity: O(n), where n is the length of the string (one pass through the string)
# Space Complexity: O(n), in the worst case all characters are '(' and are pushed onto the stack
