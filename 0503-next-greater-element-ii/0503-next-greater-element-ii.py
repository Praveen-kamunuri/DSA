class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        next_greater = [-1] * n
        
        stack = []
        
        for i in range(2 * n - 1, -1, -1):
            while stack and nums[i % n] >= stack[-1]:
                stack.pop()
            
            if i < n:
                if stack:
                    next_greater[i] = stack[-1]
                    
            stack.append(nums[i % n])
        
        return next_greater
        
            