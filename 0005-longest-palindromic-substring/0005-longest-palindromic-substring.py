class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s[0]
        res = ""
        max_len = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                sub_str = s[i:j+1]
                if sub_str == sub_str[::-1]:
                    curr_len = len(sub_str)
                    if curr_len > max_len:
                        max_len = curr_len
                        res = sub_str
                else:
                    continue
        if res == "":
            return s[0]
        else:
            return res