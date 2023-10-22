class Solution:
    def checkString(self, s: str) -> bool:
        n = len(s)
        
        if 'b' in s:
            start_ind = 0  # Initialize the start index
            
            # Find the first occurrence of 'b' and set it as the start index
            for i in range(n):
                if s[i] != 'b':
                    continue
                else:
                    start_ind = i
                    break
            
            # Check if there is any 'a' after the start index; if yes, return False
            for i in range(start_ind, n):
                if s[i] == 'a':
                    return False
            
            # If there are no 'a' characters after the first 'b', return True
            return True
        else:
            # If there are no 'b' characters in the string, return True
            return True
