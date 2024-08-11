class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt = 0
        
        word = 0
        
        for i in s:
            if i == ' ':
                if cnt != 0:
                    word = cnt
                cnt = 0
            elif 'A' <= i <=  'Z' or 'a' <= i <= 'z':
                cnt += 1
            
        if cnt != 0:
            word = cnt
        return word
    
                