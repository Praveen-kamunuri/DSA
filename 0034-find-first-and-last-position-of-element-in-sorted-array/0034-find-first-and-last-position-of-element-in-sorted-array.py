class Solution:
    def lowerBound(self, nums, target):
        n = len(nums)         # Get the length of the input 'nums' list.
        low = 0               # Initialize a low pointer to the beginning of the list.
        high = n - 1          # Initialize a high pointer to the end of the list.
        low_bound = -1        # Initialize 'low_bound' to -1 (default if the target is not found).

        while low <= high:
            mid = (low + high) // 2   # Calculate the middle index.

            if nums[mid] == target:
                low_bound = mid       # If the middle element is equal to the target, update 'low_bound' and continue searching the left half.
                high = mid - 1

            elif nums[mid] < target:
                low = mid + 1          # If the middle element is less than the target, update 'low' to search in the right half.

            else:
                high = mid - 1         # If the middle element is greater than the target, update 'high' to search in the left half.

        return low_bound

    def upperBound(self, nums, target):
        n = len(nums)         # Get the length of the input 'nums' list.
        low = 0               # Initialize a low pointer to the beginning of the list.
        high = n - 1          # Initialize a high pointer to the end of the list.
        up_bound = -1         # Initialize 'up_bound' to -1 (default if the target is not found).

        while low <= high:
            mid = (low + high) // 2   # Calculate the middle index.

            if nums[mid] == target:
                up_bound = mid        # If the middle element is equal to the target, update 'up_bound' and continue searching the right half.
                low = mid + 1

            elif nums[mid] < target:
                low = mid + 1          # If the middle element is less than the target, update 'low' to search in the right half.

            else:
                high = mid - 1         # If the middle element is greater than the target, update 'high' to search in the left half.

        return up_bound

    def searchRange(self, nums, target):
        first = self.lowerBound(nums, target)   # Find the lower bound of the target.
        second = self.upperBound(nums, target)  # Find the upper bound of the target.
        return [first, second]  # Return a list containing the lower and upper bounds.
