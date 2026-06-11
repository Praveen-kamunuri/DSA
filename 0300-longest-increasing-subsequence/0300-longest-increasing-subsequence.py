class Solution:
    def lengthOfLIS(self, nums: List[int]):

        ####################################################################
        # LONGEST INCREASING SUBSEQUENCE (LIS)
        ####################################################################

        # INTUITION
        #
        # At every index we have 2 choices:
        #
        # 1. Pick current element
        # 2. Not Pick current element
        #
        # State:
        #
        # (ind, prev_ind)
        #
        # ind      -> current index
        # prev_ind -> previously picked index
        #
        # If:
        #
        # nums[prev_ind] < nums[ind]
        #
        # then we can pick the current element.
        #
        ####################################################################
        # RECURSION
        ####################################################################
        #
        # Approach:
        #
        # Try both choices:
        #
        # 1. Not Pick
        # 2. Pick (if valid)
        #
        # Return maximum.
        #
        # TC: O(2^N)
        # SC: O(N)
        #
        # n = len(nums)
        #
        # def calLcs(ind, prev_ind):
        #
        #     if ind == n:
        #         return 0
        #
        #     not_pick = calLcs(ind + 1, prev_ind)
        #
        #     pick = 0
        #
        #     if prev_ind == -1 or nums[prev_ind] < nums[ind]:
        #         pick = 1 + calLcs(ind + 1, ind)
        #
        #     return max(pick, not_pick)
        #
        # return calLcs(0, -1)

        ####################################################################
        # MEMOIZATION
        ####################################################################
        #
        # Approach:
        #
        # Same recursion.
        #
        # Store already computed states.
        #
        # State:
        #
        # (ind, prev_ind)
        #
        # Since prev_ind can be -1,
        # coordinate shift is required.
        #
        # Column Mapping:
        #
        # -1 -> 0
        #  0 -> 1
        #  1 -> 2
        #  2 -> 3
        #
        # dp[ind][prev_ind + 1]
        #
        # TC: O(N^2)
        # SC: O(N^2) + O(N)
        #
        # n = len(nums)
        #
        # dp = [[-1 for _ in range(n + 1)] for _ in range(n)]
        #
        # def calLcs(ind, prev_ind):
        #
        #     if ind == n:
        #         return 0
        #
        #     if dp[ind][prev_ind + 1] != -1:
        #         return dp[ind][prev_ind + 1]
        #
        #     not_pick = calLcs(ind + 1, prev_ind)
        #
        #     pick = 0
        #
        #     if prev_ind == -1 or nums[prev_ind] < nums[ind]:
        #         pick = 1 + calLcs(ind + 1, ind)
        #
        #     dp[ind][prev_ind + 1] = max(pick, not_pick)
        #
        #     return dp[ind][prev_ind + 1]
        #
        # return calLcs(0, -1)

        ####################################################################
        # TABULATION
        ####################################################################
        #
        # Approach:
        #
        # Convert memo state:
        #
        # calLcs(ind, prev_ind)
        #
        # into:
        #
        # dp[ind][prev_ind + 1]
        #
        # IMPORTANT:
        #
        # prev_ind + 1
        # -> coordinate shift
        #
        # ind + 1
        # -> next recursive state
        #
        # NOT coordinate shift.
        #
        # Extra Row:
        #
        # dp[n]
        #
        # represents:
        #
        # ind == n
        #
        # whose answer is always 0.
        #
        # Fill from bottom because current row depends
        # on the next row.
        #
        # TC: O(N^2)
        # SC: O(N^2)
        #
        # n = len(nums)
        #
        # dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        #
        # for ind in range(n - 1, -1, -1):
        #
        #     for prev_ind in range(ind - 1, -2, -1):
        #
        #         not_pick = dp[ind + 1][prev_ind + 1]
        #
        #         pick = 0
        #
        #         if prev_ind == -1 or nums[prev_ind] < nums[ind]:
        #
        #             pick = 1 + dp[ind + 1][ind + 1]
        #
        #         dp[ind][prev_ind + 1] = max(pick, not_pick)
        #
        # return dp[0][0]

        ####################################################################
        # SPACE OPTIMIZATION
        ####################################################################
        #
        # Approach:
        #
        # Observe:
        #
        # dp[ind]
        #
        # only depends on:
        #
        # dp[ind + 1]
        #
        # Therefore we only keep:
        #
        # next_row   -> dp[ind + 1]
        # current_row -> dp[ind]
        #
        # TC: O(N^2)
        # SC: O(N)
        #
        ####################################################################

        n = len(nums)

        # Represents dp[ind + 1]
        next_row = [0 for _ in range(n + 1)]

        for ind in range(n - 1, -1, -1):

            # Represents dp[ind]
            current_row = [0 for _ in range(n + 1)]

            for prev_ind in range(ind - 1, -2, -1):

                # Skip current element
                not_pick = next_row[prev_ind + 1]

                # Pick current element
                pick = 0

                if prev_ind == -1 or nums[prev_ind] < nums[ind]:

                    # Current element becomes
                    # the new previous element.
                    #
                    # State:
                    #
                    # (ind + 1, ind)
                    #
                    # Column becomes:
                    #
                    # ind + 1
                    #
                    pick = 1 + next_row[ind + 1]

                current_row[prev_ind + 1] = max(pick, not_pick)

            next_row = current_row

        return next_row[0]