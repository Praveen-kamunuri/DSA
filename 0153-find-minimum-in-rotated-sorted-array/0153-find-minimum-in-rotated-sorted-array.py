import sys

class Solution(object):
    def findMin(self, nums):
        # Get the length of the input list
        n = len(nums)
        
        # Initialize pointers for binary search
        low = 0
        high = n - 1
        
        # Initialize the answer to a large value
        ans = sys.maxsize
        
        # Perform binary search
        while low <= high:
            # Calculate mid index
            mid = (low + high) // 2
            
            # Compare values at low and mid indices
            if nums[low] <= nums[mid]:
                # Update answer and adjust low pointer
                ans = min(ans, nums[low])
                low = mid + 1
            else:
                # Update answer and adjust high pointer
                ans = min(ans, nums[mid])
                high = mid - 1
        
        # Return the minimum element found
        return ans
