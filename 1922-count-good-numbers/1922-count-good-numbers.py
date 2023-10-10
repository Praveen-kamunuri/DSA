class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def power(base,powerr):
            ans = 1
            while powerr > 0:
                if powerr % 2 == 0:
                    base =  ( base * base ) % (10 ** 9 + 7)
                    powerr = powerr // 2
                else:
                    ans = (ans * base) %  ( 10 ** 9 + 7 ) 
                    powerr = powerr - 1
            return ans

        
        
        
        
        odd = n // 2
        even = n - odd
        
        ans = (power(5 , even) * power(4 , odd) ) % (10 ** 9 + 7)
        return ans
        