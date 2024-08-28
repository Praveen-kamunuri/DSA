class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        def largest_histogram(arr):
            """
            Given a list representing histogram heights, find the maximum rectangular area.
            
            Time Complexity: O(n) - Each element is pushed and popped from the stack at most once.
            Space Complexity: O(n) - Space used by the stack.
            """
            n = len(arr)
            stack = []  # Stack to store indices of histogram bars
            maxi = 0  # Variable to keep track of the maximum area
            
            for i in range(n):
                # Ensure stack has indices of bars with heights <= current bar
                while stack and arr[stack[-1]] > arr[i]:
                    height = arr[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    maxi = max(maxi, height * width)
                
                stack.append(i)
            
            # Process remaining bars in the stack
            while stack:
                height = arr[stack.pop()]
                width = n if not stack else n - stack[-1] - 1
                maxi = max(maxi, height * width)
            
            return maxi
        
        # Convert matrix from strings to integers
        matrix = [[int(cell) for cell in row] for row in matrix]
        
        n = len(matrix)  # Number of rows
        m = len(matrix[0])  # Number of columns
        
        # Initialize prefix_sum matrix to store heights of histograms
        prefix_sum = [[0] * m for _ in range(n)]
        
        max_Area = 0  # Variable to store the maximum rectangle area
        
        # Compute histogram heights for each column
        for j in range(m):
            summ = 0  # Initialize summ for each column
            for i in range(n):
                if matrix[i][j] == 0:
                    summ = 0
                else:
                    summ += 1
                prefix_sum[i][j] = summ
        
        # Compute the maximal rectangle area for each row's histogram
        for k in range(n):
            max_Area = max(max_Area, largest_histogram(prefix_sum[k]))
        
        return max_Area

# Time Complexity:
# Converting the matrix from strings to integers: O(n * m)
# Computing the prefix_sum matrix: O(n * m)
# Computing the maximal rectangle area for each row's histogram: O(n * m)
# Overall Time Complexity: O(n * m)

# Space Complexity:
# Prefix sum matrix: O(n * m)
# Stack used in largest_histogram: O(m)
# Overall Space Complexity: O(n * m)
