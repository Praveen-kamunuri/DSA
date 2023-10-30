class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)   # Get the length of the input 'nums' list.
        low = 0         # Initialize a low pointer to the beginning of the list.
        high = n - 1    # Initialize a high pointer to the end of the list.
        low_bound = n   # Initialize 'low_bound' to the length of the list (default if target is larger than all elements).
        
        while low <= high:
            mid = (low + high) // 2   # Calculate the middle index.

            if nums[mid] == target:
                return mid  # If the middle element is equal to the target, return the index of the target.

            elif nums[mid] < target:
                low = mid + 1  # If the middle element is less than the target, update 'low' to search in the right half.

            else:
                low_bound = mid   # If the middle element is greater than the target, update 'low_bound' and continue searching the left half.
                high -= 1

        return low_bound   # If the loop finishes, return the 'low_bound' which is the index where the target should be inserted.
