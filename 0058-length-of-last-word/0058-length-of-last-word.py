class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Returns the length of the last word in the input string.

        Time Complexity: O(n), where n is the length of the string `s`
        Space Complexity: O(1), no extra space used apart from variables
        """

        # Remove leading and trailing spaces
        s = s.strip()
        n = len(s)

        last_space_ind = -1  # Use -1 to represent "no space found"

        # Loop through the string to find the last space index
        for i in range(n):
            if s[i] == ' ':
                last_space_ind = i

        # If there was at least one space
        if last_space_ind != -1:
            cnt = 0
            # Count the characters after the last space
            for i in range(last_space_ind + 1, n):
                cnt += 1
            return cnt
        else:
            # If there's no space, the entire string is a single word
            return n
