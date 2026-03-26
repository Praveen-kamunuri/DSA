class Solution:
    def minInsertions(self, s: str) -> int:
        
        # INTUITION:
        # Instead of generating all subsequences and checking palindrome (costly),
        # we use a trick:
        #
        # Longest Palindromic Subsequence (LPS) = LCS(s, reverse(s))
        #
        # Why?
        # Because a palindrome reads same forward & backward,
        # so matching s with its reverse gives longest palindromic subsequence.
        #
        # Once we get LPS length:
        # Minimum insertions = total length - LPS
        #
        # Because we only need to insert missing characters to make it palindrome
        
        
        n = len(s)
        rev = s[::-1]   # reverse of string
        
        
        # Function to find LCS of s and rev
        def lcs(str1, str2, n):
            
            # dp[i][j] = LCS length of str1[0:i] and str2[0:j]
            dp = [[0] * (n + 1) for _ in range(n + 1)]
            
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    
                    # If characters match -> take diagonal +1
                    if str1[i - 1] == str2[j - 1]:
                        dp[i][j] = 1 + dp[i - 1][j - 1]
                    
                    # Else take max of left or top
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            
            return dp[n][n]
        
        
        # Longest Palindromic Subsequence length
        lps = lcs(s, rev, n)
        
        # Minimum insertions needed
        return n - lps


# Time Complexity: O(n^2)
# - We fill an n x n DP table

# Space Complexity: O(n^2)
# - DP table of size n x n