class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # Dictionary to store the next greater element for each number in nums2
        next_greater = {}
        
        # Stack to keep track of elements for which we haven't found a next greater element
        stack = []
        
        # List to store the result for nums1
        res = []
        
        # Length of nums2
        n = len(nums2)
        
        # Traverse nums2 in reverse order
        for i in range(n-1, -1, -1):
            # Pop elements from stack until we find an element greater than nums2[i]
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
                
            # If stack is empty, there is no greater element to the right
            if not stack:
                next_greater[nums2[i]] = -1
            else:
                # The top element of the stack is the next greater element
                next_greater[nums2[i]] = stack[-1]
            
            # Push the current element to the stack
            stack.append(nums2[i])
            
        # For each element in nums1, find the next greater element using the dictionary
        for num in nums1:
            res.append(next_greater[num])
        
        # Return the result list
        return res

# Time Complexity (TC): 
# The algorithm iterates through nums2 once, and for each element in nums2, it potentially 
# processes the stack elements. Each element is pushed and popped from the stack at most once.
# Hence, the time complexity is O(m + n), where m is the length of nums1, and n is the length of nums2.

# Space Complexity (SC): 
# The space complexity is O(n) due to the dictionary `next_greater` and the stack, where n is the 
# length of nums2. The result list `res` also takes O(m) space, where m is the length of nums1.
# Overall, the space complexity is O(m + n).
