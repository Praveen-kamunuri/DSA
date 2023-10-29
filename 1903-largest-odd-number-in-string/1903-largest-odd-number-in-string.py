class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        
        # Iterate through the characters of the string in reverse order
        for i in range(n-1, -1, -1):
            # Check if the integer value of the character at position i is odd
            if int(num[i]) % 2 == 1:
                # If an odd digit is found, update 'num' to keep only the prefix up to and including this digit
                num = num[0:i+1]
                return num  # Return the updated 'num'
        
        return ""  # If there are no odd digits, return an empty string
