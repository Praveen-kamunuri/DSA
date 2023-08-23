class Solution(object):
    def singleNonDuplicate(self, nums):
        n = len(nums)
        
        # Edge cases for arrays of size 1 or non-duplicate elements at the ends
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n - 1] != nums[n - 2]:
            return nums[n - 1]
        
        # Binary search loop to find the single non-duplicate element
        low = 1
        high = n - 2
        while low <= high:
            mid = (low + high) // 2
            
            # Check if nums[mid] is the single non-duplicate element
            if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]
            
            # Handle cases where we are in the left or right side of the array
            if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
                # Eliminate the left half
                low = mid + 1
            else:
                # Eliminate the right half
                high = mid - 1
        
        # If no single non-duplicate element is found
        return -1
