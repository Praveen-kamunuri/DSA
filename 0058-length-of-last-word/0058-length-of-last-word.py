class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        n = len(s)
        
        word_len = 0
        
        i = n - 1
        
        while i >= 0:
            
            
            if s[i] == ' ':
                if word_len == 0:
                    i -= 1
                else:
                    return word_len
            else:
                word_len += 1
                i -= 1
        return word_len
                
        
        
        