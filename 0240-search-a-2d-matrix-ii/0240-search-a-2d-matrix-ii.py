class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Helper function to perform binary search on a sorted array
        def binSearch(arr, target):
            n = len(arr)
            low = 0
            high = n - 1
            
            # Binary search loop
            while low <= high:
                mid = (low + high) // 2
                
                # Check if the mid element is the target
                if arr[mid] == target:
                    return True
                
                # If target is greater, ignore left half
                elif arr[mid] < target:
                    low = mid + 1
                    
                # If target is smaller, ignore right half
                else:
                    high = mid - 1
                    
            # Target is not present in the array
            return False
        
        row = len(matrix)  # Number of rows in the matrix
        
        # Iterate through each row and apply binary search
        for i in range(row):
            if binSearch(matrix[i], target):
                return True
        
        # Target is not found in any row
        return False

# Time Complexity: O(M * log N)
# Space Complexity: O(1)

# Explanation:
# - M is the number of rows in the matrix.
# - N is the number of columns in each row.
# - For each row, binary search takes O(log N) time.
# - As there are M rows, the overall time complexity is O(M * log N).
# - Space complexity is O(1) because we are not using any additional space that scales with the input size.
