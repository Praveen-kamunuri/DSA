from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        # ----------------------------------------------------------
        # Intuition:
        #
        # In the normal LIS problem, we only store the length of the
        # longest increasing subsequence ending at every index.
        #
        # Here, that is not enough because there can be multiple LIS
        # having the same maximum length.
        #
        # So for every index we maintain:
        #
        # dp[i]  -> Length of the Longest Increasing Subsequence
        #           ending at index i.
        #
        # cnt[i] -> Number of LIS having length dp[i] and ending
        #           exactly at index i.
        #
        # While checking all previous indices:
        #
        # Case 1:
        # If we find a strictly longer LIS,
        # update the length and copy the count.
        #
        # Case 2:
        # If we find another way to achieve the same maximum length,
        # simply add its count.
        #
        # Finally, several indices may have the overall maximum LIS
        # length, so sum all of their counts.
        # ----------------------------------------------------------

        n = len(nums)

        # Every element itself is an LIS of length 1.
        dp = [1] * n

        # Initially, there is exactly one way to form that LIS.
        cnt = [1] * n

        # Stores the overall maximum LIS length.
        maxi = 1

        # Compute dp[] and cnt[]
        for i in range(n):

            # Try extending every previous subsequence.
            for j in range(i):

                # Can extend the increasing subsequence.
                if nums[j] < nums[i]:

                    # --------------------------------------------------
                    # Found a longer LIS ending at i.
                    #
                    # Replace the old length.
                    # Since this is the best length so far,
                    # inherit the number of ways from j.
                    # --------------------------------------------------
                    if dp[j] + 1 > dp[i]:

                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]

                    # --------------------------------------------------
                    # Found another LIS with the SAME maximum length.
                    #
                    # Add the number of ways from j because this is
                    # another distinct path to reach the same length.
                    # --------------------------------------------------
                    elif dp[j] + 1 == dp[i]:

                        cnt[i] += cnt[j]

            # Keep track of overall LIS length.
            maxi = max(maxi, dp[i])

        # Sum counts of all indices whose LIS length equals maximum.
        res = 0

        for i in range(n):
            if dp[i] == maxi:
                res += cnt[i]

        return res


# Time Complexity:
# O(N²)
#
# Two nested loops are used to compute dp[] and cnt[].
#
# Final traversal to sum the answer is O(N).
#
# Overall:
# O(N²)


# Space Complexity:
# O(N)
#
# dp[]  -> O(N)
# cnt[] -> O(N)
#
# Total:
# O(N)