class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        stack = []
        
        next_greater = [0] * n
        
        i = 2 * n - 1
        
        for i in range(2 * (n-1), -1, -1):
            
            while stack and nums[i % n] >= stack[-1]:
                stack.pop()
                
            
            if i < n:
                
                if not stack:
                    next_greater[i] = -1
                
                else:
                    next_greater[i] = stack[-1]
                    
            stack.append(nums[i % n])
            
        return next_greater
                    
            
                
        