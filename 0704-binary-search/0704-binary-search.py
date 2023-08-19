class Solution(object):
    def search(self, nums, target):
        n = len(nums)  # Get the length of the input array
        low = 0        # Initialize the low index for binary search
        high = n - 1   # Initialize the high index for binary search
        
        while low <= high:  # Continue the binary search while low index is less than or equal to high index
            mid = (low + high) // 2  # Calculate the middle index
            
            if nums[mid] == target:  # If the middle element is equal to the target
                return mid  # Return the index of the target
                
            elif nums[mid] < target:  # If the middle element is less than the target
                low = mid + 1  # Move the low index to mid + 1 to search the right half
                
            else:  # If the middle element is greater than the target
                high = mid - 1  # Move the high index to mid - 1 to search the left half
                
        return -1  # If the target is not found in the array, return -1
