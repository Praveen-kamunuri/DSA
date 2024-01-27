from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Helper function to check if a substring can be segmented
        def canSegment(substring):
            # If the result for the current substring is already memoized, return it
            if substring in memo:
                return memo[substring]

            # If the current substring is in the word dictionary, it can be segmented
            if substring in wordDict:
                memo[substring] = True
                return True

            # Check all possible splits of the current substring
            for i in range(1, len(substring)):
                prefix = substring[:i]
                suffix = substring[i:]
                # If the prefix is in the word dictionary and the suffix can be segmented, return True
                if prefix in wordDict and canSegment(suffix):
                    memo[substring] = True
                    return True

            # If no valid segmentation is found, memoize and return False
            memo[substring] = False
            return False

        memo = {}  # Memoization to store results of subproblems
        return canSegment(s)
