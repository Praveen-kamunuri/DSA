class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        res = ' '.join(s[::-1])
        return res
        