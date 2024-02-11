class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def search(i, j, n, m, word, board, k):
            if k == len(word):
                return True
            
            if i < 0 or j < 0 or i == n or j == m or board[i][j] != word[k]:
                return False
            
            ch = board[i][j]
            
            board[i][j] = '#'
            
            op1 = search(i-1, j, n, m, word, board, k+1)
            op2 = search(i+1, j, n, m, word, board, k+1)
            op3 = search(i, j+1, n, m, word, board, k+1)
            op4 = search(i, j-1, n, m, word, board, k+1)
            
            if op1 or op2 or op3 or op4:
                return True
            
            board[i][j] = ch
            
        
        n = len(board)
        m = len(board[0])
        
        for i in range(n):
            for j in range(m):
                if search(i, j, n, m, word, board, 0):
                    return True
                
                
        return False
        