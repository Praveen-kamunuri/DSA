class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        
        stack = []
        
        max_Area = 0
        
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                ele = heights[stack[-1]]
                stack.pop()
                nse = i
                pse = -1
                if stack:
                    pse = stack[-1]
                    
                max_Area = max(max_Area, ele * (nse - pse - 1))
            stack.append(i)
            
        while stack:
            nse = len(heights)
            ele = stack[-1]
            stack.pop()
            pse = -1
            if stack:
                pse = stack[-1]
                
            max_Area = max(max_Area, heights[ele] * (nse - pse - 1))
            
        return max_Area
            