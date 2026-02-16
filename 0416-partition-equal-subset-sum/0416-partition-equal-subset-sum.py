class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Step 1: Calculate total sum of array
        total_sum = 0
        n = len(nums)

        for i in range(n):
            total_sum += nums[i]
        
        # If total sum is odd, we cannot divide it into two equal subsets
        if total_sum % 2 == 1:
            return False
        
        # Target sum for each subset
        target = total_sum // 2

        # DP table:
        # dp[i][t] means:
        # Using elements from index i to n-1,
        # can we make sum = t ?
        # -1  -> not computed yet
        # True/False -> already computed result
        dp = [[-1] * (target + 1) for _ in range(n + 1)]
 

        def find_Equal_subset_sum(ind, target, dp):

            # Base Case 1:
            # If target becomes 0, we found a valid subset
            if target == 0:
                return True
            
            # Base Case 2:
            # If we reached end of array and target != 0
            if ind == n:
                return False
            
            # If already computed, return stored value
            if dp[ind][target] != -1:
                return dp[ind][target]

            take = False

            # Option 1: Take current element (if it does not exceed target)
            if nums[ind] <= target:
                take = find_Equal_subset_sum(ind + 1, target - nums[ind], dp)
            
            # Option 2: Do not take current element
            not_take = find_Equal_subset_sum(ind + 1, target, dp)

            # Store result in DP table
            dp[ind][target] = take or not_take

            return dp[ind][target]

        return find_Equal_subset_sum(0, target, dp)


"""
Time Complexity (TC):
O(n * target)

Reason:
There are n indices and target possible sums.
Each state (ind, target) is computed only once due to memoization.

Space Complexity (SC):
O(n * target)  -> DP table
O(n)           -> Recursion stack space

Overall Space: O(n * target)
"""
