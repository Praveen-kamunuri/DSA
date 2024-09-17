class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hash_arr = [-1] * 255
        l = 0
        r = 0
        max_len = 0
        
        while r < n:
            if hash_arr[ord(s[r])] != -1:
                if hash_arr[ord(s[r])] >= l:
                    l = hash_arr[ord(s[r])] + 1
            curr_len = (r - l) + 1
            max_len = max(curr_len, max_len)
            hash_arr[ord(s[r])] = r
            r += 1
        return max_len
        