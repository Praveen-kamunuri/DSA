# Approach:
# - First, sort the array to allow the use of the two-pointer technique.
# - Initialize the closest sum (`res`) with the sum of the first three elements.
# - For each element in the array (up to the third last), fix it as the first number of the triplet.
# - Use two pointers (`start` and `end`) to find the other two numbers such that their sum
#   is closest to the target.
# - If the exact target is found, return immediately.
# - Otherwise, update the closest sum whenever a closer one is found.
# - Move pointers based on whether the current sum is less than or greater than the target.

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # Sort the array to apply two-pointer technique
        nums.sort()

        # Initialize the result with the sum of the first three numbers
        res = nums[0] + nums[1] + nums[2]

        # Loop through each element up to the third last
        for curr in range(n - 2):
            start = curr + 1
            end = n - 1

            # Use two-pointer approach to find closest sum
            while start < end:
                temp = nums[curr] + nums[start] + nums[end]

                # If exact match found, return immediately
                if temp == target:
                    return temp

                # Update result if current sum is closer to target
                if abs(temp - target) < abs(res - target):
                    res = temp

                # Move pointers based on comparison
                if temp < target:
                    start += 1
                else:
                    end -= 1

        # Return the closest sum found
        return res


# Time Complexity: O(n^2)
# - Outer loop runs O(n) times
# - Inner while loop runs O(n) in total for each outer iteration
# - So total is O(n^2)

# Space Complexity: O(1)
# - No extra space used except for a few variables
# - Sorting is done in-place
