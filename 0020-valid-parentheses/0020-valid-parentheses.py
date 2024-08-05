class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        for i in s:
            if i == '(' or i ==  '[' or i == '{':
                stack.append(i)
            else:
                if not stack:
                    return False
                
                ch = stack.pop()
                
                if i == ')' and ch != '(':
                    return False
                elif i == ']' and ch != '[':
                    return False
                elif i == '}' and ch != '{':
                    return False
                
        return len(stack) == 0
                    
                    
                