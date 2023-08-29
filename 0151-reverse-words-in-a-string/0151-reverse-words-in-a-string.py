class Solution(object):
    def reverseWords(self, s):
        stri = s.split()
        stri.reverse()
        rev_str = ' '.join(stri)
        return rev_str