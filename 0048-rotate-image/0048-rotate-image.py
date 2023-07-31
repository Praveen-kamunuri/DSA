class Solution(object):
    def rotate(self, matrix):
        rows = len(matrix)# Calculate the number of rows in the input matrix and assign it to the variable "rows".
        res = []
        # Initialize an empty list "res" which will be used to store the rotated matrix.

        for i in range(rows):
            # Start a loop that iterates over each row of the input matrix.

            temp = []
            # Initialize an empty list "temp" which will be used to store the elements of the current row after the rotation.

            for j in range(rows):
                # Start a nested loop that iterates over each element in the current row.

                temp.insert(0, matrix[j][i])
                # Insert the element at position [j][i] (row j, column i) of the original matrix into the "temp" list at the beginning.
                # This effectively transposes the matrix (interchanging rows and columns) as it traverses each row.

            res.append(temp)
            # Append the "temp" list (which represents the transposed row) to the "res" list.
            # This creates a transposed version of the entire matrix.

        for i in range(rows):
            for j in range(rows):
                matrix[i][j] = res[i][j]
        # After the first loop completes, "res" will contain the transposed version of the original matrix.
        # This double loop then goes through the "matrix" again and replaces each element in "matrix" with the corresponding element from the "res" list.
        # This effectively rotates the matrix 90 degrees clockwise.

        # The "rotate" method does not return anything explicitly, as it modifies the original "matrix" in place.
