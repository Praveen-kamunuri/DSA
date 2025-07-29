class Solution:
    def countMaxOrSubsets(self, nums):
        # max_or stores the maximum OR value found so far among all subsets
        max_or = 0
        # count stores the number of subsets that have the OR value equal to max_or
        count = 0

        def dfs(index, current_or):
            nonlocal max_or, count
            # Base case: if we've considered all elements
            if index == len(nums):
                if current_or == max_or:
                    # If this subset's OR matches the current max OR, increment count
                    count += 1
                elif current_or > max_or:
                    # If this subset's OR is new maximum, reset count
                    max_or = current_or
                    count = 1
                return
            # Include nums[index] in the subset and update OR value
            dfs(index + 1, current_or | nums[index])
            # Exclude nums[index] from the subset and keep OR value same
            dfs(index + 1, current_or)

        # Start DFS with index 0 and OR value 0
        dfs(0, 0)
        return count


# ----------------------
# ✅ Example:
# nums = [3, 1]
# Subsets: [], [3], [1], [3,1]
# Their ORs: 0, 3, 1, 3 → max OR is 3, and it occurs in [3] and [3,1] → count = 2

# \U0001f50d Time Complexity: O(2^n)
# - Because we explore all subsets (each element has include/exclude option).
# - For n = len(nums), total calls = 2^n.

# \U0001f9e0 Space Complexity: O(n)
# - Due to recursion stack in DFS (depth can go up to n).
