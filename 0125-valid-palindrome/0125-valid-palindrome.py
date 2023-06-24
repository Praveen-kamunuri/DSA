class Solution(object):
    def isPalindrome(self, s):
        # Convert to lowercase and remove non-alphanumeric characters
        modified = ''.join(c.lower() for c in s if c.isalnum())
        
        # Compare with the reversed string
        return modified == modified[::-1]