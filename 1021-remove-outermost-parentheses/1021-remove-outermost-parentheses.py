class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        n = len(s)
        
        res = ''
        
        bal = 0
        
        for i in range(n):
            if s[i] == '(':
                bal += 1
                
                if bal > 1:
                    res += s[i]
                    
            else:
                bal -= 1
                
                if bal > 0:
                    res += s[i]
                    
        return res
        