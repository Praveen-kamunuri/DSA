class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Find the shortest string in the list using the 'min' function with the 'key' parameter
        min_str = min(strs, key=len)
        
        # Iterate through the characters of the shortest string
        for i, char in enumerate(min_str):
            # For each character at index 'i' in the shortest string,
            # check if it matches the corresponding character in other strings in the list
            for s in strs:
                if s[i] != char:
                    # If a character doesn't match, return the common prefix found so far
                    return s[:i]
        
        # If all characters matched in the shortest string, return the shortest string itself
        return min_str
