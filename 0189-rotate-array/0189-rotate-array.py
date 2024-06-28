from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        
        n = len(nums)  # Get the length of the array
        
        k = k % n  # Handle the case when k is greater than n
        
        # Step 1: Reverse the entire array
        nums[:] = nums[::-1]
        
        # Step 2: Reverse the first k elements
        nums[:k] = nums[:k][::-1]
        
        # Step 3: Reverse the remaining n-k elements
        nums[k:] = nums[k:][::-1]
        
        

        # Time Complexity: O(n)
        # Space Complexity: O(1) (in-place rotation)
