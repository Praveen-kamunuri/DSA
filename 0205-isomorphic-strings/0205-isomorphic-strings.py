class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Check if the lengths of both strings are different; if so, they cannot be isomorphic.
        if len(s) != len(t):
            return False
        
        # Initialize two dictionaries to store mappings from characters in s to characters in t, and vice versa.
        s_map = {}  # Mapping from s to t
        t_map = {}  # Mapping from t to s
        
        # Iterate through the characters in the strings s and t using their indices.
        for i in range(len(s)):
            char_s = s[i]  # Get the current character in s.
            char_t = t[i]  # Get the current character in t.
            
            # Check if the character from s is already in the s_map.
            if char_s in s_map:
                # If it is, check if the mapping to t is consistent with the current character in t.
                if s_map[char_s] != char_t:
                    return False  # If not, the strings are not isomorphic, so return False.
            else:
                # If the character from s is not in the s_map, add it with the mapping to the current character in t.
                s_map[char_s] = char_t
            
            # Similarly, check if the character from t is already in the t_map.
            if char_t in t_map:
                # If it is, check if the mapping to s is consistent with the current character in s.
                if t_map[char_t] != char_s:
                    return False  # If not, the strings are not isomorphic, so return False.
            else:
                # If the character from t is not in the t_map, add it with the mapping to the current character in s.
                t_map[char_t] = char_s
        
        # If the loop completes without any issues, the strings are isomorphic, so return True.
        return True
