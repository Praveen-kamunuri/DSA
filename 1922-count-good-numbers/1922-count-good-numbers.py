class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def power(x, y):
            result = 1
            while y > 0:
                if y % 2 == 1:
                    result = (result * x) % MOD
                x = (x * x) % MOD
                y //= 2
            return result

        # Calculate counts for even and odd positions using exponentiation
        even_counts = power(5, (n + 1) // 2)
        odd_counts = power(4, n // 2)

        # Calculate the total count
        result = (even_counts * odd_counts) % MOD

        return result
