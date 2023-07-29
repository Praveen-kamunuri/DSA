class Solution(object):
    def rotate(self, matrix):
        rows = len(matrix)
        res = []
        for i in range(rows):
            temp = []
            for j in range(rows):
                temp.insert(0,matrix[j][i])
            res.append(temp)
        for i in range(rows):
            for j in range(rows):
                matrix[i][j] = res[i][j]
                
        
        
        