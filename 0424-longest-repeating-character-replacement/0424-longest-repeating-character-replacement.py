class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        hash_arr = [0] * 26
        max_freq = 0
        n = len(s)
        max_len = 0
        while r < n:
            hash_arr[ord(s[r]) - ord('A')] += 1
            
            max_freq = max(max_freq, hash_arr[ord(s[r]) - ord('A')] )
            
            while (r - l + 1) - max_freq > k:
                hash_arr[ord(s[l]) - ord('A')] -= 1
                max_freq = 0
                for i in hash_arr:
                    if i > max_freq:
                        max_freq = max(max_freq, i)
                l += 1
            
            if (r - l + 1) - max_freq <= k:
                max_len = max(max_len, (r - l + 1) )
            r += 1
        return max_len
                
                
            
            
            
            
            