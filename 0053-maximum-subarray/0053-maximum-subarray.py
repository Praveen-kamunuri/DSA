class Solution(object):
    def maxSubArray(self, nums):
        # Initialize max_sum and current_sum with the first element of the array
        max_sum = nums[0]
        current_sum = nums[0]

        # Iterate over the array starting from the second element
        for i in range(1, len(nums)):
            # Calculate the new current_sum by choosing the maximum between the current element and the sum of the current element and previous subarray
            current_sum = max(nums[i], current_sum + nums[i])

            # Update max_sum if the current_sum is greater
            max_sum = max(max_sum, current_sum)

        # Return the maximum sum found
        return max_sum

       