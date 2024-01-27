from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Helper function to check if a substring can be segmented
        def canSegment(substring):
            if substring in memo:
                return memo[substring]

            if substring in wordDict:
                memo[substring] = True
                return True

            for i in range(1, len(substring)):
                prefix = substring[:i]
                suffix = substring[i:]
                if prefix in wordDict and canSegment(suffix):
                    memo[substring] = True
                    return True

            memo[substring] = False
            return False

        memo = {}  # Memoization to store results of subproblems
        return canSegment(s)