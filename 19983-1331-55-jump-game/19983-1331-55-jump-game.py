class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize the maximum index that can be reached
        max_index = 0

        # Iterate through the array
        for i in range(len(nums)):
            # If the current index is beyond the maximum reachable index, 
            # it is not possible to jump to this position
            if i > max_index:
                return False

            # Update the maximum reachable index based on the current position and jump length
            max_index = max(max_index, i + nums[i])

        # If we can iterate through the array without returning False, it means the last index is reachable
        return True

# Time Complexity Analysis:
# The algorithm iterates through the array once, making it O(n), where n is the length of the nums array.

# Space Complexity Analysis:
# The algorithm uses a constant amount of extra space, making it O(1).
