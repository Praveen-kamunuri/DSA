class Solution:
    def isHappy(self, n: int) -> bool:
        
        sett = set()
        
        def func(num):
            res = 0
            while num != 0:
                rem = num % 10
                num = num // 10 
                res += rem ** 2
            return res
        
        
        while n != 1:
            
            n = func(n)
            
            
            
            if n in sett:
                return False
            
            sett.add(n)
            
        return True
        