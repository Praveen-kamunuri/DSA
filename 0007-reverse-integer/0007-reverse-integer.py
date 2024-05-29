class Solution:
    def reverse(self, x: int) -> int:
        
        sign = 1
        if x < 0:
            sign = -1
            
            x = abs(x)
        
        c = 0
        
        while x > 0:
            rem = x % 10
            c = c * 10 + rem
            x = x // 10
            
        res = c * sign
        
        if -2 ** 31 <= res <= (2 ** 31) - 1:
            return res
        else:
            return 0
        