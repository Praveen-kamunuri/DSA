class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        rev_str = s[::-1]
        return ' '.join(rev_str)