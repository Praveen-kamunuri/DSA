class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        n = len(s)
        
        bal = 0
        
        res = []
        
        mystr = ''
        
        for i in range(n):
            
            if s[i] == '(':
                bal += 1
                
                if bal > 1:
                    res.append(s[i])
            else:
                bal -= 1
                
                if bal > 0:
                    res.append(')')
                    
        for i in res:
            mystr += i
        return mystr
        
        