class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        def power(base,exp):
            res = 1
            while exp > 0:
                if exp % 2 == 0:
                    base = (base * base) % ( 10 ** 9 + 7)
                    exp = exp // 2
                else:
                    res = (res * base) % (10 ** 9 + 7)
                    exp = exp - 1
            return res
        
        
        
        odd = n // 2
        even = n - odd
        
        ans = ( power(5 , even) * power(4 ,odd) )   % ( 10 ** 9 + 7)
        return ans