class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        
        def find_small_range(nums, n):
            
            
            prev_small_index = [-1] * n
            
            stack = []
            
            for i in range(n):
                while stack and nums[stack[-1]] > nums[i]:
                    stack.pop()
                
                if stack:
                    prev_small_index[i] = stack[-1]
                
                stack.append(i)
            
            stack = []
            
            next_small_index = [n] * n
            
            for i in range(n-1, -1, -1):
                while stack and nums[stack[-1]] >= nums[i]:
                    stack.pop()
                if stack:
                    next_small_index[i] = stack[-1]
                    
                stack.append(i)
                
                
            total = 0
            for i in range(n):
                left_count = i - prev_small_index[i]
                right_count = next_small_index[i] - i
                
                total += (left_count * right_count) * nums[i]
                
            return total
        
        
        def find_large_range(nums, n):
            
            
            prev_large_index = [-1] * n
            
            stack = []
            
            for i in range(n):
                while stack and nums[stack[-1]] < nums[i]:
                    stack.pop()
                
                if stack:
                    prev_large_index[i] = stack[-1]
                
                stack.append(i)
            
            stack = []
            
            next_large_index = [n] * n
            
            for i in range(n-1, -1, -1):
                while stack and nums[stack[-1]] <= nums[i]:
                    stack.pop()
                if stack:
                    next_large_index[i] = stack[-1]
                    
                stack.append(i)
                
                
            total = 0
            for i in range(n):
                left_count = i - prev_large_index[i]
                right_count = next_large_index[i] - i
                
                total += (left_count * right_count) * nums[i]
                
            return total
                
                
            
            
        
        
        
        
        n = len(nums)
        small_range = find_small_range(nums,n)
        large_range = find_large_range(nums, n)
        
        return large_range - small_range
        