class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Length of main string (haystack)
        x = len(haystack)
        # Length of substring (needle)..
        y = len(needle)

        # Loop through all possible starting positions
        # We only need to check until (x - y) index,
        # because beyond that there aren't enough chars left to match needle
        for i in range(x - y + 1):
            # Extract substring of length y from haystack starting at index i
            # Compare it with needle
            if haystack[i:i+y] == needle:
                return i   # Return first matching index
        
        # If no match found after loop ends
        return -1


# Time Complexity (TC): O((x - y + 1) * y) ≈ O(x * y) in worst case
#   - For each possible index (x - y + 1), we may compare up to y characters
# Space Complexity (SC): O(1)
#   - We only use a few variables (x, y, i), no extra space that grows with input
