class Solution:
    def countMaxOrSubsets(self, nums):
        max_or = 0
        count = 0

        def dfs(index, current_or):
            nonlocal max_or, count
            if index == len(nums):
                if current_or == max_or:
                    count += 1
                elif current_or > max_or:
                    max_or = current_or
                    count = 1
                return
            # Include nums[index]
            dfs(index + 1, current_or | nums[index])
            # Exclude nums[index]
            dfs(index + 1, current_or)

        dfs(0, 0)
        return count
