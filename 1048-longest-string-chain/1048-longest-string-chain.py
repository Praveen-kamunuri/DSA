from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        ========================================================================
        PROBLEM INTUITION:
        ------------------
        The problem asks us to find the longest string chain where each word is a 
        predecessor of the next (obtained by inserting exactly one character).
        
        Since order in the chain depends purely on the length of the words 
        (a word of length L can only be a predecessor to a word of length L + 1), 
        the relative original positions in the array do not matter for forming 
        subsequences. Therefore, we first sort the array based on word length.
        
        Once sorted, this transforms into a classic variant of the Longest 
        Increasing Subsequence (LIS) problem! Instead of checking if `arr[ind] > arr[prev_ind]`,
        we check if `words[prev_ind]` can form `words[ind]` by inserting exactly 1 character 
        using our helper function `isok`.
        ========================================================================
        """
        
        # Sort words by length so that potential predecessors always come before successors
        words.sort(key=len)
        n = len(words)

        # Helper function to check if 'small' is a direct predecessor of 'large'
        def isok(small: str, large: str) -> bool:
            if len(small) == len(large):
                return False
            
            cnt = 0
            i, j = 0, 0
            
            while i <= (len(small) - 1) and j <= (len(large) - 1):
                if small[i] == large[j]:
                    i += 1
                    j += 1
                else:
                    cnt += 1  # Found a mismatch/inserted character
                    j += 1
                
            if j != len(large):
                cnt += len(large) - j 

            if cnt > 1:
                return False
            else:
                return True


        # ========================================================================
        # APPROACH 1: BRUTE FORCE RECURSION (Commented Out)
        # ------------------------------------------------------------------------
        # Intuition: 
        # For every word at index `ind`, we have two choices:
        # 1. Not Pick: Skip the current word and keep the previous picked word (`prev_ind`).
        # 2. Pick: If it's the first word (`prev_ind == -1`) or a valid successor (`isok == True`),
        #    we can include it and update `prev_ind` to `ind`.
        #
        # DP State:
        # `calLSC(ind, prev_ind)` -> Max chain length from index `ind` to `n-1` 
        # given that the last picked word was at index `prev_ind`.
        #
        # Complexity:
        # Time Complexity: O(2^n * L) where L is the maximum length of a word (due to string matching).
        # Space Complexity: O(n) for the recursion stack frame depth.
        # ========================================================================
        """
        def calLSC_recursion(ind, prev_ind):
            if ind == n:
                return 0

            # Option 1: Do not pick the current word
            not_pick = 0 + calLSC_recursion(ind + 1, prev_ind)

            # Option 2: Pick the current word (if valid)
            pick = 0
            if prev_ind == -1 or isok(words[prev_ind], words[ind]):
                pick = 1 + calLSC_recursion(ind + 1, ind)
            
            return max(pick, not_pick)

        return calLSC_recursion(0, -1)
        """


        # ========================================================================
        # APPROACH 2: TOP-DOWN MEMOIZATION (Commented Out)
        # ------------------------------------------------------------------------
        # Intuition:
        # The recursive tree contains many overlapping subproblems. We can store 
        # computed states in a 2D matrix `dp[n][n+1]`.
        #
        # Coordinate Shift:
        # `prev_ind` ranges from `-1` to `n-1`. Since array indices cannot be negative, 
        # we shift `prev_ind` by +1 when storing/retrieving from the DP table. 
        # Thus, `prev_ind == -1` is stored at index `0`, and `prev_ind == k` is stored at `k + 1`.
        #
        # Complexity:
        # Time Complexity: O(n^2 * L) -> n * n states, each taking O(L) for string comparison.
        # Space Complexity: O(n^2) for the DP table + O(n) for the recursive stack.
        # ========================================================================
        """
        dp = [[-1 for _ in range(n + 1)] for _ in range(n)]

        def calLSC_memo(ind, prev_ind):
            if ind == n:
                return 0

            # Coordinate shift: prev_ind + 1 used for lookup
            if dp[ind][prev_ind + 1] != -1:
                return dp[ind][prev_ind + 1]

            not_pick = 0 + calLSC_memo(ind + 1, prev_ind)

            pick = 0
            if prev_ind == -1 or isok(words[prev_ind], words[ind]):
                pick = 1 + calLSC_memo(ind + 1, ind)
            
            dp[ind][prev_ind + 1] = max(pick, not_pick)
            return dp[ind][prev_ind + 1]

        return calLSC_memo(0, -1)
        """


        # ========================================================================
        # APPROACH 3: BOTTOM-UP TABULATION (Commented Out)
        # ------------------------------------------------------------------------
        # Intuition & Direction:
        # In recursion, `ind` goes from `0` to `n`, and the base case is at `ind == n`.
        # Tabulation moves in the exact opposite direction: from bottom to top (`n-1` down to `0`).
        #
        # Transition & Coordinate Shift:
        # To avoid negative index crashes, `prev_ind` loop runs from `ind-1` down to `-1`, 
        # and we map it to the DP table using `prev_ind + 1`.
        # `dp[ind][prev_ind + 1] = max(pick, not_pick)`
        #
        # Complexity:
        # Time Complexity: O(n^2 * L) -> Nested loops running roughly n*n/2 times with O(L) operations.
        # Space Complexity: O(n^2) -> Size of the 2D DP grid.
        # ========================================================================
        """
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for ind in range(n - 1, -1, -1):
            for prev_ind in range(ind - 1, -2, -1):
                # Not pick takes the result from the next row (ind + 1)
                not_pick = 0 + dp[ind + 1][prev_ind + 1]

                # Pick takes the result from the next row with current index as new predecessor
                pick = 0
                if prev_ind == -1 or isok(words[prev_ind], words[ind]):
                    pick = 1 + dp[ind + 1][ind + 1]

                dp[ind][prev_ind + 1] = max(pick, not_pick)

        return dp[0][0]
        """


        # ========================================================================
        # APPROACH 4: SPACE OPTIMIZATION (ACTIVE EXECUTABLE SOLUTION)
        # ------------------------------------------------------------------------
        # Intuition:
        # Look closely at the Tabulation transition:
        # To calculate `dp[ind][prev_ind + 1]`, we ONLY reference values from `dp[ind + 1]`.
        # We never look at any row beyond `ind + 1`. 
        #
        # Why Space Optimization Works:
        # Instead of allocating an entire 2D matrix of size `(n + 1) x (n + 1)`, we can 
        # maintain just two rows: `next_row` (representing `ind + 1`) and `curr_row` 
        # (representing `ind`). After finishing a row, `curr_row` becomes the `next_row` 
        # for the subsequent step.
        #
        # Complexity:
        # Time Complexity: O(n^2 * L) -> Two nested loops tracking states, with O(L) string validation.
        # Space Complexity: O(n) -> Optimized down from O(n^2) to just two rows of size n + 1.
        # ========================================================================
        
        # next_row represents the state at (ind + 1)
        next_row = [0 for _ in range(n + 1)]
        
        # Traverse backwards from the last word down to the first word
        for ind in range(n - 1, -1, -1):
            curr_row = [0 for _ in range(n + 1)]
            for prev_ind in range(ind - 1, -2, -1):
                
                # Option 1: Do not pick the current word
                not_pick = 0 + next_row[prev_ind + 1]

                # Option 2: Pick the current word
                pick = 0
                if prev_ind == -1 or isok(words[prev_ind], words[ind]):
                    pick = 1 + next_row[ind + 1]

                # Save the maximum chain length attainable into the current state configuration
                curr_row[prev_ind + 1] = max(pick, not_pick)
            
            # Move the row pointer upward for the next iteration
            next_row = curr_row

        # The answer accumulates at the start state where ind = 0 and prev_ind = -1 (shifted to 0)
        return next_row[0]