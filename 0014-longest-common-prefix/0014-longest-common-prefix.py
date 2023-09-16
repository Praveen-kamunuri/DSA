class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or strs[0] == "":
            return ""
        if len(strs) == 1:
            return strs[0]
        
        
        
        
        min_str = min(strs , key = len)
        for i , char in enumerate(min_str):
            for s in strs:
                if s[i] != char:
                    return min_str[:i]
        return min_str

            
            

        