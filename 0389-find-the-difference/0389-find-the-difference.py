class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Initialize result with 0 (since 0 ^ x = x)
        result = 0
        
        # XOR all characters in both strings
        for char in s:
            result ^= ord(char)
        for char in t:
            result ^= ord(char)
        
        # The result will be the ASCII value of the added character
        return chr(result)
