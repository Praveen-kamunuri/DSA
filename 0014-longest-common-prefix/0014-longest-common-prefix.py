class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Check if the input list is empty or contains an empty string
        if not strs or strs[0] == "":
            return ""
        
        # Check if there's only one string in the list
        if len(strs) == 1:
            return strs[0]
        
        # Find the shortest string in the array (lexicographically)
        min_str = min(strs, key=len)
        
        # Iterate through the characters of the shortest string
        for i, char in enumerate(min_str):
            # Compare the current character with the corresponding character in each string in 'strs'
            for s in strs:
                if s[i] != char:
                    # If a mismatch is found, return the common prefix up to this point
                    return min_str[:i]
        
        # If no mismatches are found, return the entire shortest string as the common prefix
        return min_str
