class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(steps):
            # If we reach exactly 0 steps left, it's one valid way
            if steps == 0:
                return 1
            # If steps go negative, it's not valid
            if steps < 0:
                return 0
            # If result is already computed, return it
            if steps in memo:
                return memo[steps]

            # Take 1 step or 2 steps
            memo[steps] = dfs(steps - 1) + dfs(steps - 2)
            return memo[steps]

        return dfs(n)
