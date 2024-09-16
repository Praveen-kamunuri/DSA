from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)  # Get the length of the input list
        max_len = 0  # To store the length of the longest subarray found
        l = 0  # Left pointer of the sliding window
        r = 0  # Right pointer of the sliding window
        zeros = 0  # Count of zeros in the current window
        
        # Iterate with the right pointer over the list
        while r < n:
            # If the current element is zero, increment the zero count
            if nums[r] == 0:
                zeros += 1
            
            # If the number of zeros exceeds k, move the left pointer to reduce zeros
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1  # Move the left pointer to the right
            
            # Calculate the length of the current valid window
            curr_len = r - l + 1
            # Update max_len if the current window is larger
            max_len = max(curr_len, max_len)
            
            # Move the right pointer to the next element
            r += 1
        
        # Return the length of the longest subarray found
        return max_len

# Time Complexity (TC): O(n)
# The time complexity is O(n) because each element is processed at most twice (once by the right pointer and once by the left pointer).
# Space Complexity (SC): O(1)
# The space complexity is O(1) because only a few extra variables are used, and the space used does not scale with the input size.
