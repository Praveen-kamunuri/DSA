class Solution:
    def fib(self, n: int) -> int:

        dp = [-1] * (n + 1)

        def fib_dp(num):
            if num <= 1:
                return num

            if dp[num] != -1:
                return dp[num]
            
            dp[num] = fib_dp(num - 1) + fib_dp(num - 2)

            return dp[num]


        return fib_dp(n)


        