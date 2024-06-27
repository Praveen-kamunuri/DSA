class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Check if the input string has a length of 1, in which case it's already a palindrome.
        if len(s) == 1:
            return s[0]
        
        res = ""        # Initialize an empty string to store the longest palindrome found.
        max_len = 0     # Initialize a variable to keep track of the maximum palindrome length.

        # Iterate through the characters of the input string using two nested loops.
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                sub_str = s[i:j+1]  # Extract a substring from the input string.
                
                # Check if the substring is a palindrome (equal to its reverse).
                if sub_str == sub_str[::-1]:
                    curr_len = len(sub_str)  # Calculate the length of the current palindrome substring.
                    
                    # Update the maximum palindrome length and result string if necessary.
                    if curr_len > max_len:
                        max_len = curr_len
                        res = sub_str
                else:
                    continue  # If the substring is not a palindrome, continue searching.

        # If no palindrome is found, return the first character of the input string.
        if res == "":
            return s[0]
        else:
            return res
