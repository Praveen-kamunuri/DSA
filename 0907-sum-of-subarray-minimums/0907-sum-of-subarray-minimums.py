from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        
        # Helper function to find indices of the Previous Smaller Element (PLE) for each element
        def findPrev_small(arr, n):
            res = [-1] * n  # Initialize array to store the index of previous smaller elements
            stack = []  # Stack to keep track of indices
            
            # Iterate over each element to determine PLE
            for i in range(n):
                while stack and arr[stack[-1]] > arr[i]:
                    stack.pop()  # Remove elements from stack that are greater than the current element
                if stack:
                    res[i] = stack[-1]  # Update PLE index for the current element
                stack.append(i)  # Push the current index onto the stack
                
            return res
        
        # Helper function to find indices of the Next Smaller Element (NSE) for each element
        def findNext_small(arr, n):
            res = [n] * n  # Initialize array to store the index of next smaller elements
            stack = []  # Stack to keep track of indices
            
            # Iterate over each element from right to left to determine NSE
            for i in range(n-1, -1, -1):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()  # Remove elements from stack that are greater than or equal to the current element
                if stack:
                    res[i] = stack[-1]  # Update NSE index for the current element
                stack.append(i)  # Push the current index onto the stack
                
            return res
        
        # Calculate Previous Smaller Element indices
        prev_smaller_index = findPrev_small(arr, n)
        
        # Calculate Next Smaller Element indices
        next_smaller_index = findNext_small(arr, n)
        
        mod = 10**9 + 7  # Define modulus for the result to prevent overflow
        
        total = 0  # Initialize total sum
        
        # Iterate through each element to compute its contribution
        for i in range(n):
            left_subArr_count = i - prev_smaller_index[i]  # Number of subarrays where arr[i] is the minimum to the left
            right_subArr_count = next_smaller_index[i] - i  # Number of subarrays where arr[i] is the minimum to the right
            
            total += arr[i] * (left_subArr_count * right_subArr_count)  # Compute contribution of arr[i]
            total %= mod  # Take modulo to prevent overflow
        
        return total

# Time Complexity (TC): O(n), where n is the length of the input array
# Space Complexity (SC): O(n), due to the space used by the `prev_smaller_index`, `next_smaller_index`, and `stack`
