class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        n = len(s)
        
        if len(s) != len(t):
            
            return False
        
        s_map = {}
        t_map = {}
        
        
        
        for i in range(n):
            char_s = s[i]

            char_t = t[i]
            
            if char_s in s_map:
                if s_map[char_s] != char_t:
                    return False
                
            else:
                s_map[char_s] = char_t
                
            
            
            if char_t in t_map:
                if t_map[char_t] != char_s:
                    return False
            
            else:
                
                t_map[char_t] = char_s
        return True
                
                