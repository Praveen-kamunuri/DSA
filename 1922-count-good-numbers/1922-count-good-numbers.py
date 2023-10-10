class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        def power(base, exp):
            res = 1
            while exp > 0:
                if exp % 2 == 0:
                    base = (base * base) % (10 ** 9 + 7)  # Square base and apply modulo if exp is even
                    exp = exp // 2
                else:
                    res = (res * base) % (10 ** 9 + 7)  # Multiply res by base and apply modulo if exp is odd
                    exp = exp - 1
            return res
        
        odd = n // 2  # Calculate the count of odd digits
        even = n - odd  # Calculate the count of even digits
        
        ans = (power(5, even) * power(4, odd)) % (10 ** 9 + 7)  # Calculate the count of "good numbers" with modulo
        return ans  # Return the result
