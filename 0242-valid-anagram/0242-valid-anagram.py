class Solution(object):
    def isAnagram(self, s, t):
        # Sort the characters of both strings and compare if they are equal
        if sorted(s) == sorted(t):
            return True  # If sorted strings are equal, strings are anagrams
        else:
            return False  # If sorted strings are not equal, strings are not anagrams
