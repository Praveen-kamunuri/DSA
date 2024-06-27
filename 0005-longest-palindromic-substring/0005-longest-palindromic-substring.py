class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        if n == 1:
            return s[0]
        
        max_len = 0
        
        res = ''
        
        for i in range(n):
            for j in range(i+1,n):
                sub_str = s[i:j+1]
                
                if sub_str == sub_str[::-1]:
                    curr_len = len(sub_str)
                    
                    if curr_len > max_len:
                        max_len = curr_len
                        res = sub_str
                    
        if res == "":
            return s[0]
        
        else:
            return res
                
                
                    
                