from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # If there are fewer than or equal to 4 numbers, we can make them all the same in 3 moves
        if len(nums) <= 4:
            return 0
        
        # Sort the array
        nums.sort()
        
        # Initialize the minimum difference to a large value
        min_diff = float('inf')
        
        # Consider four cases:
        # 1. Remove the three largest elements
        min_diff = min(min_diff, nums[-4] - nums[0])
        # 2. Remove the two largest elements and the smallest element
        min_diff = min(min_diff, nums[-3] - nums[1])
        # 3. Remove the largest element and the two smallest elements
        min_diff = min(min_diff, nums[-2] - nums[2])
        # 4. Remove the three smallest elements
        min_diff = min(min_diff, nums[-1] - nums[3])
        
        return min_diff
