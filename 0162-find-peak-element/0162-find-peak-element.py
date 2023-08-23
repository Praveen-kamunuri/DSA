class Solution(object):
    def findPeakElement(self, nums):
        n = len(nums)
        
        # Edge cases for arrays of size 1 or peaks at the ends
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n - 1] > nums[n - 2]:
            return n - 1
        
        # Binary search loop to find the peak element
        low = 1
        high = n - 2
        while low <= high:
            mid = (low + high) // 2
            
            # Check if nums[mid] is a peak element
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid - 1]:
                # Search in the right half
                low = mid + 1
            elif nums[mid] > nums[mid + 1]:
                # Search in the left half
                high = mid - 1
            else:
                # If we are in between the two peaks , go either way!. I choose right!
                low = mid + 1
        
        # If no peak element is found
        return -1
