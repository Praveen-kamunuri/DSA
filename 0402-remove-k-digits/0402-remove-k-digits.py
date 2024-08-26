class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        n = len(num)
        
        res = ""
        
        stack = []
        
        for char in num:
            while stack and k > 0 and  int(stack[-1]) > int(char):
                stack.pop()
                
                k -= 1
            stack.append(char)
        
        while k > 0:
            stack.pop()
            k -= 1
        
        if not stack:
            return "0"
        
        res = ""
        
        while stack:
            res += stack.pop()
        if len(res) == 1 and res == '0':
            return '0'
        while len(res) > 1 and res[-1] == '0':
            res = res[:-1]
        
        return res[::-1]
        