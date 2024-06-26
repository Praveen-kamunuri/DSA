class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Early exit if lengths of s and t are different
        if len(s) != len(t):
            return False
        
        n = len(s)
        
        # Initialize arrays to count character frequencies ('a' to 'z')
        s_arr = [0] * 26
        t_arr = [0] * 26
        
        # Count frequencies of characters in string s
        for i in range(n):
            s_arr[ord(s[i]) - ord('a')] += 1
        
        # Count frequencies of characters in string t
        for i in range(n):
            t_arr[ord(t[i]) - ord('a')] += 1
        
        # Compare the two arrays
        return s_arr == t_arr

    
    """
        Checks if two strings s and t are anagrams of each other.
        
        Time complexity: O(n)
        Space complexity: O(1), since the arrays s_arr and t_arr are of fixed size (26)
        where n is the length of the strings s and t.
    """
