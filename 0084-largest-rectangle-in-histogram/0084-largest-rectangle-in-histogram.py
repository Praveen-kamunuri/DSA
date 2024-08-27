class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        def find_prev_small(arr, n):
            res = [-1] * n
            
            stack = []
            for i in range(n):
                
                while stack and arr[stack[-1]] > arr[i]:
                    stack.pop()
                    
                if stack:
                    res[i] = stack[-1]
                
                stack.append(i)
            return res
                
        def find_next_small(arr, n):
            res = [n] * n
            
            stack = []
            
            for i in range(n-1, -1, -1):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                    
                if stack:
                    res[i] = stack[-1]
                
                stack.append(i)
            return res
        
        
        
        n = len(heights)
        
        
        prev_small_index = find_prev_small(heights, n)
        
        next_small_index = find_next_small(heights, n)
        
        maxi = 0
        
        for i in range(n):
            
            maxi = max(maxi, (next_small_index[i] - prev_small_index[i] - 1) * heights[i] ) 
        
        return  maxi
            