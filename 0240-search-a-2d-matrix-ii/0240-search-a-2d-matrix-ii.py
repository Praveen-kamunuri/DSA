class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        def binSearch(arr, target):
            n = len(arr)
            
            low = 0
            
            high = n - 1
            
            while low <= high:
                mid = (low + high) // 2
                
                if arr[mid] == target:
                    return True
                
                
                elif arr[mid] < target:
                    low = mid + 1
                    
                else:
                    high = mid - 1
                    
            return False
                    
        
        
        
        row = len(matrix)
        
        for i in range(row):
            if binSearch(matrix[i], target):
                return True
        
        return False
                
        