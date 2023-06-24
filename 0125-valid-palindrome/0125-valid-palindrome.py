class Solution(object):
    def isPalindrome(self, s):
        modifi = ''.join(c.lower() for c in s if c.isalnum())
        return modifi == modifi[::-1]