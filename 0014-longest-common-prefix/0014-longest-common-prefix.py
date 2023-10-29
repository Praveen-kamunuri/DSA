class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        min_str = min(strs,key = len)
        for i , char in enumerate(min_str):
            for s in strs:
                if s[i] != char:
                    return s[:i]
        return min_str
            