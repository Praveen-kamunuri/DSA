from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)  # Length of the input list
        
        stack = []  # Initialize an empty stack
        
        next_greater = [0] * n  # Initialize the result array with 0s
        
        # Loop through the array twice (simulate circular array)
        for i in range(2 * n - 1, -1, -1):
            
            # Ensure the stack contains only elements greater than the current element
            while stack and nums[i % n] >= stack[-1]:
                stack.pop()  # Pop smaller elements as they aren't the next greater element
            
            # If we are in the first pass (i < n), update the next greater element
            if i < n:
                # If stack is empty, no greater element exists, assign -1
                if not stack:
                    next_greater[i] = -1
                else:
                    # Otherwise, assign the top of the stack as the next greater element
                    next_greater[i] = stack[-1]
            
            # Push the current element (considering circular behavior using i % n) onto the stack
            stack.append(nums[i % n])
        
        # Return the array containing the next greater elements
        return next_greater

# Time Complexity (TC): O(n)
# Each element is processed twice (2n iterations) and pushed/popped from the stack at most once.

# Space Complexity (SC): O(n)
# The space is used by the 'stack' and 'next_greater' array, both of size n.
