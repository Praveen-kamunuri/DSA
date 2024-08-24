class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        n = len(arr)
        
        
        def findPrev_small(arr, n):
            
            res = [-1] * n
            
            stack = []
            
            for i in range(n):
                while stack and arr[stack[-1]] > arr[i]:
                    stack.pop()
                    
                if stack:
                    res[i] = stack[-1]
                stack.append(i)
                
                
            return res
                
        def findNext_small(arr, n):
            res = [n] * n
            
            stack = []
            
            for i in range(n-1, -1, -1):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                
                if stack:
                    res[i] = stack[-1]
                
                stack.append(i)
                
            return res
                    
        
        prev_smaller_index = findPrev_small(arr, n)
        
        next_smaller_index = findNext_small(arr, n)
        
        mod = (10 ** 9) + 7
        
        stack = []
        
        total = 0
        
        for i in range(n):
            left_subArr_count = i - prev_smaller_index[i]
            right_subArr_count = next_smaller_index[i] - i
            
            total += arr[i] * (left_subArr_count * right_subArr_count)
            
            total %= mod
            
        return total
            
            
            
        