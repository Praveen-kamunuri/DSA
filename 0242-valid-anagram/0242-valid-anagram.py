class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        n = len(s)
        
        s_arr = [0] * 26
        
        t_arr = [0] * 26
        
        for i in range(n):
            s_arr[ord(s[i]) - ord('a')] += 1
            
            t_arr[ord(t[i]) - ord('a')] += 1
        
        return s_arr == t_arr
            
            