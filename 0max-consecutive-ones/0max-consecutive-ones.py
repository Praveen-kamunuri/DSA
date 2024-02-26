class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Initialize variables to keep track of the current count and the maximum count of consecutive ones
        cnt = 0  # Current count
        maxi = 0  # Maximum count
        
        # Iterate through the elements in the list
        for i in range(len(nums)):
            if nums[i] == 1:
                # If the current element is 1, increment the current count
                cnt += 1
                # Update the maximum count if the current count is larger
                maxi = max(maxi, cnt)
            else:
                # If the current element is 0, reset the current count to 0
                cnt = 0
        
        # Return the maximum count of consecutive ones
        return maxi
