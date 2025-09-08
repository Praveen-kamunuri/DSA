class Solution:
    def getNoZeroIntegers(self, n: int) -> [int]:
        def has_zero(x):
            while x > 0:
                if x % 10 == 0:
                    return True
                x //= 10
            return False
        
        for a in range(1, n):
            b = n - a
            if not has_zero(a) and not has_zero(b):
                return [a, b]
