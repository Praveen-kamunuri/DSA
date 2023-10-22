class Solution:
    def checkString(self, s: str) -> bool:
        n = len(s)
        if  'b' in s:
            start_ind = 0
            for  i in range(n):
                if s[i] != 'b':
                    continue
                else:
                    start_ind = i
                    break
            for i in range(start_ind,n):
                if s[i] == 'a':
                    return False
            return True
        else:
            return True
            
        
        

        