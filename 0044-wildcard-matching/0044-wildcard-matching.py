class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        n = len(s)
        m = len(p)

        dp = [[-1 for _ in range(m + 1)]for _ in range(n + 1)]

        def isAllStars(n, s):
            for i in range(n + 1):
                if s[i] != '*':
                    return 0
            return 1

        def wildCardHelper(i, j, s1, s2, dp):

            if i < 0 and j < 0:
                return 1

            if i < 0 and  j >= 0:
                return isAllStars(j, s2)

            if j < 0 and i >= 0:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]
            
            if s1[i] == s2[j] or s2[j] == '?':
                if wildCardHelper(i - 1, j - 1, s1, s2, dp) == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
                return dp[i][j]


            elif s2[j] == '*':

                if wildCardHelper(i - 1, j, s1, s2, dp) == 1 or wildCardHelper(i, j - 1, s1, s2, dp) == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0

                return dp[i][j] 
            
            else:
                dp[i][j] = 0
                return dp[i][j]

        return wildCardHelper(n - 1, m - 1, s, p, dp) == 1
      