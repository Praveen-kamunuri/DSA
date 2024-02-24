class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        m = len(board)
        n = len(board[0])
        
        def search(i, j, m, n, board, word, k):
            if k == len(word):
                return True
            
            if i < 0 or j < 0 or i == m or j == n or board[i][j] != word[k]:
                return False
            
            ch = board[i][j]
            
            board[i][j] = '*'
            
            top = search(i - 1, j, m, n, board, word, k+1)
            bot = search(i + 1, j, m, n, board, word, k+1)
            left = search(i, j - 1,m , n, board, word, k + 1)
            right = search(i, j + 1, m, n, board, word, k+1)
            
            board[i][j] = ch
            
            return top or bot or left or right
        
        
        for i in range(m):
            for j in range(n):
                if search(i, j, m, n, board, word, 0):
                    return True
        return False