class Solution(object):
    def start_ind(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        first = -1  # Initialize the index for the first occurrence of the target
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                first = mid  # Update the first occurrence index and continue searching on the left side
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return first
    
    def end_ind(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        end = -1  # Initialize the index for the last occurrence of the target
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                end = mid  # Update the last occurrence index and continue searching on the right side
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return end
                
                
    def searchRange(self, nums, target):
        start = self.start_ind(nums, target)  # Get the index of the first occurrence of the target
        end = self.end_ind(nums, target)  # Get the index of the last occurrence of the target
        return [start, end]  # Return the indices of the target's occurrences
