class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs or strs[0] == "":
            return ""
        if len(strs) == 1:
            return strs[0]

        # Find the shortest string in the array (lexicographically)
        shortest_str = min(strs, key=len)

        for i, char in enumerate(shortest_str):
            for s in strs:
                if s[i] != char:
                    return shortest_str[:i]

        return shortest_str  # Return the shortest string if it's the common prefix

