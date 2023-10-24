class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        
        # Initialize three pointers: low, mid, and high
        low = 0  # Pointer for 0s
        mid = 0  # Pointer for 1s
        high = n - 1  # Pointer for 2s
        
        # Use the Dutch National Flag algorithm to efficiently sort the array
        while mid <= high:
            # If the current element is 0, swap it with the element at the low pointer
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1  # Increment low to move to the next position for 0s
                mid += 1  # Increment mid to consider the next element
                
            # If the current element is 1, simply increment mid to the next element
            elif nums[mid] == 1:
                mid += 1
                
            # If the current element is 2, swap it with the element at the high pointer
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1  # Decrement high to move to the next position for 2s
                
        # At the end of the loop, the array is sorted with 0s, 1s, and 2s in ascending order using the Dutch National Flag algorithm
