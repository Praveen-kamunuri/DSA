from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}  # Dictionary to store next greater elements for each element in nums2
        stack = []  # Stack to keep track of elements for which we need to find the next greater element

        # Traverse nums2 from right to left
        for i in range(len(nums2) - 1, -1, -1):
            # Pop elements from the stack that are less than or equal to the current element
            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            # If stack is not empty, the top of the stack is the next greater element
            if stack:
                next_greater[nums2[i]] = stack[-1]
            else:
                next_greater[nums2[i]] = -1

            # Push the current element to the stack
            stack.append(nums2[i])

        # Construct the result for nums1 using the next_greater dictionary
        res = [next_greater[num] for num in nums1]
        
        return res

# Time Complexity (TC): O(n + m)
# - O(n) for traversing the nums2 array where n = len(nums2).
# - O(m) for constructing the result where m = len(nums1).
# - Overall, the time complexity is O(n + m).

# Space Complexity (SC): O(n)
# - O(n) for storing the next_greater dictionary, where n = len(nums2).
# - O(n) for the stack in the worst case.
# - Overall, the space complexity is O(n).
