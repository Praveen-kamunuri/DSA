class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(i, j, n, m, board, word, k):
            if k == len(word):
                return True
            if i < 0 or j < 0 or i == n  or j == m or board[i][j]  != word[k]:
                return False    
            
            ch = board[i][j]
            
            board[i][j] = '#'
            
            op1 = search(i+1,j,n,m,board,word,k+1)
            op2 = search(i,j+1,n,m,board,word,k+1)
            op3 = search(i-1,j,n,m,board,word,k+1)
            op4 = search(i,j-1,n,m,board,word,k+1)
            
            board[i][j] = ch
            return op1 or op2 or op3 or op4 
        
        
        
        
        n = len(board) # n
        m = len(board[0])# m
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if search(i,j,n,m,board,word,0):
                        return True
                        