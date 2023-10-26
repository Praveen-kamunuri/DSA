class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)  # Get the size of the matrix

        # Transpose the matrix (swap elements across the main diagonal)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row to complete the 90-degree rotation
        for i in range(n):
            matrix[i].reverse()
