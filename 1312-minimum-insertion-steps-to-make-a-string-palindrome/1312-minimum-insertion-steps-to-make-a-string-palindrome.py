class Solution:
    def minInsertions(self, s: str) -> int:

        n = len(s)

        rev_s = s[::-1]

       
        def findLCS(s, rev_s, n):

            dp = [[0] * (n + 1)for _ in range(n + 1)]

            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    if s[i - 1] == rev_s[j - 1]:
                        dp[i][j] = 1 + dp[i - 1][j - 1]

                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

            return dp[n][n]


        longest_pal =  findLCS(s, rev_s, n)

        return n - longest_pal