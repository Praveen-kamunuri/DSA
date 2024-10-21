class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        cnt = 0
        hash_arr = [0] * 256
        min_len = float('inf')
        start_ind = -1
        
        n = len(s)
        m = len(t)
        
        for i in t:
            hash_arr[ord(i)] += 1
        
        while r < n:
            if hash_arr[ord(s[r])] > 0:
                cnt += 1
            
            hash_arr[ord(s[r])] -= 1
            
            while cnt == m:
                
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    start_ind = l
            
                hash_arr[ord(s[l])] += 1
                if hash_arr[ord(s[l])] > 0:
                    cnt -= 1
                
                l += 1
            r += 1
        
        if start_ind == -1:
            return ""
        else:
            return s[start_ind:start_ind + min_len]
        
            
                
                    
                
        