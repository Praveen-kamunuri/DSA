class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        n = len(s)
        
        cnt = 0
        
        hash_arr = [-1] * 3
        
        for i in range(n):
            hash_arr[ord(s[i]) - ord('a')] = i
            
            if hash_arr[0] != -1 and  hash_arr[1] != -1 and hash_arr[2] != -1:
                cnt += min(hash_arr) + 1
        return cnt
                
        