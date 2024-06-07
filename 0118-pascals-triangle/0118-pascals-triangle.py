class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        triangle = [[1], [1,1]]
        
        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1], [1,1]]
        
        
        for i in range(numRows - 2):
            
            row = [1]
            
            for j in range(len(triangle[-1]) - 1):
                
                row.append(triangle[-1][j] + triangle[-1][j+1])
                
            row.append(1)
            triangle.append(row)
            
        return triangle
        