class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        
        # If string length is 1, it's the only unique character
        if n == 1:
            return 0
        
        # Dictionary to store character counts
        hashmap = {}
        
        # Step 1: Count occurrences of each character in the string
        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1
        
        # Step 2: Find the index of the first unique character
        for i, char in enumerate(s):
            if hashmap[char] == 1:
                return i
        
        # If no unique character found, return -1
        return -1

# Time complexity: O(n), where n is the length of the string s
# Space complexity: O(1) or O(26), since the hashmap will hold at most 26 keys (for lowercase English letters)
