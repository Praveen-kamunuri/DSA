from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        def solve(nums, k):
            # If k is negative, there can't be any valid subarray
            if k < 0:
                return 0
            
            n = len(nums)  # Length of the input list
            l = 0          # Left pointer for the window
            summ = 0       # Count of odd numbers in the current window
            cnt = 0        # Count of valid subarrays
            
            # Iterate over the array with right pointer r
            for r in range(n):
                # Increment summ if the current number is odd
                summ += nums[r] % 2
                
                # Shrink the window from the left until we have at most k odd numbers
                while summ > k:
                    summ -= nums[l] % 2  # Remove the leftmost element's contribution
                    l += 1  # Move the left pointer to the right
                
                # Count the number of valid subarrays ending at r
                cnt += r - l + 1
            
            return cnt
        
        # Calculate the number of subarrays with exactly k odd numbers
        return solve(nums, k) - solve(nums, k - 1)

# Time Complexity: O(n), where n is the length of the nums array.
# Space Complexity: O(1), as we are using only a constant amount of extra space.