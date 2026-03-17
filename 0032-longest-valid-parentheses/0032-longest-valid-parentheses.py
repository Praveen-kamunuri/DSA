class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Initialize counters for left and right parentheses and max length
        left = 0
        right = 0
        max_len = 0

        # First pass: Left to Right
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            # If both counters are equal, it's a valid substring
            if left == right:
                max_len = max(max_len, 2 * right)
            # If there are more ')' than '(', reset counters
            elif right > left:
                left = right = 0

        # Reset counters for the second pass
        left = 0
        right = 0

        # Second pass: Right to Left
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')':
                right += 1
            else:
                left += 1

            # If both counters are equal, it's a valid substring
            if left == right:
                max_len = max(max_len, 2 * left)
            # If there are more '(' than ')', reset counters
            elif left > right:
                left = right = 0

        return max_len

# Time Complexity: O(n), where n is the length of the string (2 passes over the string)
# Space Complexity: O(1), only constant space used for counters