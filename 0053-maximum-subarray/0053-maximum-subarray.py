class Solution(object):
    def maxSubArray(self, nums):
        cur_sum = 0  # Variable to keep track of the current sum
        maxi = nums[0]  # Variable to store the maximum sum found so far, initialized with the first element of the array
        for i in range(len(nums)):  # Iterate through the elements of the array
            cur_sum += nums[i]  # Add the current element to the current sum
            
            if cur_sum > maxi:  # If the current sum is greater than the maximum sum found so far
                maxi = cur_sum  # Update the maximum sum to the current sum
            
            if cur_sum < 0:  # If the current sum becomes negative
                cur_sum = 0  # Reset the current sum to 0 (start a new subarray)
        
        return maxi  # Return the maximum sum found
