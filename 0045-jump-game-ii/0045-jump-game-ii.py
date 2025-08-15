from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        # Get the length of the input array
        n = len(nums)
        
        # If the array has only one element, no jumps are needed..
        if n == 1:
            return 0
        
        # Initialize variables to track the number of jumps, the farthest reachable index, 
        # and the current range end (end of the current jump)
        jumps = 0
        farthest = 0
        current_end = 0
        
        # Loop through the array until the second-to-last index.
        for i in range(n - 1):
            # Update the farthest index reachable from this position
            farthest = max(farthest, i + nums[i])
            
            # If we reach the end of the current jump range
            if i == current_end:
                # Increment the jump count
                jumps += 1
                # Move the current end to the farthest index reachable so far
                current_end = farthest
                
                # If the farthest index is beyond or at the last index, break out of the loop
                if current_end >= n - 1:
                    break
        
        # Return the total number of jumps needed to reach the last index
        return jumps
