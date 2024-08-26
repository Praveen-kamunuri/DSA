class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # Function to calculate the total contribution of the smallest elements in all subarrays
        def find_small_range(nums, n):
            # Array to store the index of the previous smaller element for each element in nums
            prev_small_index = [-1] * n
            
            # Stack to maintain indices of elements in a decreasing order for comparison
            stack = []
            
            # Loop to calculate previous smaller indices
            for i in range(n):
                # Pop elements from the stack until we find an element smaller than nums[i]
                while stack and nums[stack[-1]] > nums[i]:
                    stack.pop()
                
                # If stack is not empty, assign the top element as the previous smaller element's index
                if stack:
                    prev_small_index[i] = stack[-1]
                
                # Push the current index onto the stack
                stack.append(i)
            
            # Reset the stack for calculating next smaller indices
            stack = []
            
            # Array to store the index of the next smaller element for each element in nums
            next_small_index = [n] * n
            
            # Loop to calculate next smaller indices (from right to left)
            for i in range(n-1, -1, -1):
                # Pop elements from the stack until we find an element smaller than or equal to nums[i]
                while stack and nums[stack[-1]] >= nums[i]:
                    stack.pop()
                
                # If stack is not empty, assign the top element as the next smaller element's index
                if stack:
                    next_small_index[i] = stack[-1]
                    
                # Push the current index onto the stack
                stack.append(i)
                
            # Variable to store the total contribution of all subarray minimums
            total = 0
            for i in range(n):
                # Calculate the number of subarrays in which nums[i] is the minimum element
                left_count = i - prev_small_index[i]
                right_count = next_small_index[i] - i
                
                # Add the contribution of nums[i] as the minimum element in these subarrays
                total += (left_count * right_count) * nums[i]
            
            # Return the total sum of contributions of the minimum elements
            return total
        
        # Function to calculate the total contribution of the largest elements in all subarrays
        def find_large_range(nums, n):
            # Array to store the index of the previous larger element for each element in nums
            prev_large_index = [-1] * n
            
            # Stack to maintain indices of elements in an increasing order for comparison
            stack = []
            
            # Loop to calculate previous larger indices
            for i in range(n):
                # Pop elements from the stack until we find an element larger than nums[i]
                while stack and nums[stack[-1]] < nums[i]:
                    stack.pop()
                
                # If stack is not empty, assign the top element as the previous larger element's index
                if stack:
                    prev_large_index[i] = stack[-1]
                
                # Push the current index onto the stack
                stack.append(i)
            
            # Reset the stack for calculating next larger indices
            stack = []
            
            # Array to store the index of the next larger element for each element in nums
            next_large_index = [n] * n
            
            # Loop to calculate next larger indices (from right to left)
            for i in range(n-1, -1, -1):
                # Pop elements from the stack until we find an element larger than or equal to nums[i]
                while stack and nums[stack[-1]] <= nums[i]:
                    stack.pop()
                
                # If stack is not empty, assign the top element as the next larger element's index
                if stack:
                    next_large_index[i] = stack[-1]
                    
                # Push the current index onto the stack
                stack.append(i)
                
            # Variable to store the total contribution of all subarray maximums
            total = 0
            for i in range(n):
                # Calculate the number of subarrays in which nums[i] is the maximum element
                left_count = i - prev_large_index[i]
                right_count = next_large_index[i] - i
                
                # Add the contribution of nums[i] as the maximum element in these subarrays
                total += (left_count * right_count) * nums[i]
            
            # Return the total sum of contributions of the maximum elements
            return total
        
        # Main logic to calculate the result
        n = len(nums)
        
        # Calculate the sum of all minimum contributions
        small_range = find_small_range(nums, n)
        
        # Calculate the sum of all maximum contributions
        large_range = find_large_range(nums, n)
        
        # Subtract the total contribution of minimums from the total contribution of maximums
        return large_range - small_range


# Time Complexity (TC):
# - Each of the `find_small_range` and `find_large_range` functions runs in O(n).
# - This is because each element is pushed and popped from the stack at most once.
# - Therefore, the overall time complexity is O(n) + O(n) = O(n).

# Space Complexity (SC):
# - The space complexity is O(n) due to the usage of the `prev_small_index`, `next_small_index`, `prev_large_index`, `next_large_index`, and the stack.
# - Thus, the total space complexity is O(n).
