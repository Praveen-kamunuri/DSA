class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # Define a recursive function for searching the word on the board
        def search(i, j, n, m, board, word, k):
            # If the entire word has been found, return True
            if k == len(word):
                return True

            # Check if the current position is out of bounds or if the character at this position
            # does not match the current character in the word
            if i < 0 or j < 0 or i == n or j == m or board[i][j] != word[k]:
                return False

            # Save the current character on the board, and mark it as visited using a temporary character '#'
            ch = board[i][j]
            board[i][j] = '#'

            # Recursively check in all four directions (up, down, left, right)
            op1 = search(i + 1, j, n, m, board, word, k + 1)
            op2 = search(i, j + 1, n, m, board, word, k + 1)
            op3 = search(i - 1, j, n, m, board, word, k + 1)
            op4 = search(i, j - 1, n, m, board, word, k + 1)

            # Restore the original character on the board
            board[i][j] = ch

            # Return True if any of the recursive calls returned True
            return op1 or op2 or op3 or op4

        # Get the dimensions of the board
        n = len(board)
        m = len(board[0])

        # Iterate through each cell in the board and start the search from that cell
        for i in range(n):
            for j in range(m):
                if search(i, j, n, m, board, word, 0):
                    return True

        # If no match is found, return False
        return False
