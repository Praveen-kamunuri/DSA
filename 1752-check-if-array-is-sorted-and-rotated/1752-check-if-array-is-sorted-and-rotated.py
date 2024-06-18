from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        """
        This function checks if the given array nums can be sorted in non-decreasing order
        by rotating the array. It returns True if it can be, otherwise False.
        """
        
        n = len(nums)  # Get the length of the list
        
        peek = 0  # Initialize the counter for the number of "peaks"
        
        # Iterate through the list to count the number of times an element is greater than the next element
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                peek += 1
                
        # Check if the last element is greater than the first element, indicating a potential peak at the end
        if nums[n-1] > nums[0]:
            peek += 1
            
        # If there is at most one peak, the array can be sorted by rotating
        if peek <= 1:
            return True
        else:
            return False

# Time Complexity (TC):
# The time complexity is O(n) where n is the number of elements in the list nums.
# This is because we are iterating through the list once to count the number of peaks.

# Space Complexity (SC):
# The space complexity is O(1) because we are using only a constant amount of extra space 
# (variables n and peek) regardless of the size of the input list nums.
