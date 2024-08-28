class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        
        
        
        def largest_histogram(arr):
            n = len(arr)
            
            stack = []
            
            maxi = 0
            
            for i in range(n):
                while stack and arr[stack[-1]] > arr[i]:
                    element = arr[stack.pop()]
                    next_small_ind = i
                    pre_small_ind = -1
                    if stack:
                        pre_small_ind = stack[-1]
                    
                    maxi = max(maxi, (next_small_ind - pre_small_ind - 1) * element)
                    
                stack.append(i)
            
            while stack:
                element = arr[stack.pop()]
                next_small_ind = n
                pre_small_ind = -1
                if stack:
                    pre_small_ind = stack[-1]
                
                maxi = max(maxi, (next_small_ind - pre_small_ind - 1) * element)
            
            return maxi
                
                    
                    
                
            
            
            
            
        
        matrix = [[int(cell) for cell in row] for row in matrix]
        
        n = len(matrix)
        
        m = len(matrix[0])
        
        prefix_sum = [[0] * m for _ in range(n)]
        
        max_Area = 0
        
        for j in range(m):
            summ = 0
            for i in range(n):
                summ += matrix[i][j]
                if matrix[i][j] == 0:
                    summ = 0
                else:
                    prefix_sum[i][j] = summ
            
        for k in range(n):
            max_Area = max(max_Area, largest_histogram(prefix_sum[k]))
        return max_Area
            
            