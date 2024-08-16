class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Length of the input list
        n = len(nums)
        
        # Initialize the result list with -1 for each element
        next_greater = [-1] * n
        
        # Stack to keep track of elements whose next greater element is not found yet
        stack = []
        
        # Traverse the array in reverse order twice to handle the circular nature of the problem
        for i in range(2 * n - 1, -1, -1):  # i goes from 2n-1 to 0
            
            # While stack is not empty and the current element is greater or equal to the top of the stack
            while stack and nums[i % n] >= stack[-1]:
                stack.pop()  # Pop smaller elements from the stack
                
            # Since we're interested in filling next_greater only in the first pass (i < n)
            if i < n:
                # If stack is not empty, the top of the stack is the next greater element
                if stack:
                    next_greater[i] = stack[-1]
            
            # Push the current element onto the stack
            stack.append(nums[i % n])
        
        # Return the list of next greater elements for each position
        return next_greater


# Time Complexity (TC): 
# - O(n) for the loop, which iterates 2 * n times in total.
# - Each element is pushed and popped from the stack at most once.
# - Overall TC: O(n)

# Space Complexity (SC):
# - O(n) for the stack and the result list (`next_greater`).
# - Overall SC: O(n)
