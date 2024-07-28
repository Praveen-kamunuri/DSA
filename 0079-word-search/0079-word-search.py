class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def search(n, m, board, word, i, j, k):
            if k == len(word):
                return True
            
            
            if i < 0 or j < 0 or i == n or j == m or board[i][j] != word[k]:
                return False
            
            
            ch = board[i][j]
            
            board[i][j] = '#'
            
            op1 = search(n, m, board, word, i + 1, j, k + 1)
            op2 = search(n, m, board, word, i, j + 1, k + 1)
            op3 = search(n, m, board, word, i - 1, j, k + 1)
            op4 = search(n, m, board, word, i, j - 1, k + 1)
            
            board[i][j] = ch
    
            
            return op1 or op2 or op3 or op4
        
        
        
        n = len(board)
        
        m = len(board[0])
        
        for i in range(n):
            for j in range(m):
                if search(n, m, board, word, i, j, 0):
                    return True
        return False