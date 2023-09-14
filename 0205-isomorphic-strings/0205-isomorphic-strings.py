# Define a class named Solution
class Solution(object):
    # Define a method named isIsomorphic that takes two strings s and t as input
    def isIsomorphic(self, s, t):
        # Check if the lengths of the input strings s and t are not equal
        if len(s) != len(t):
            # If the lengths are different, return False since they cannot be isomorphic
            return False
        
        # Initialize an empty dictionary s_hashmap to store mappings from s to t
        s_hashmap = {}
        # Initialize an empty dictionary t_hashmap to store mappings from t to s
        t_hashmap = {}
        
        # Iterate through pairs of characters from s and t using the zip function
        for i, j in zip(s, t):
            # Check if the character i from s is already in s_hashmap
            if i in s_hashmap:
                # If it is, check if the mapping in s_hashmap for i is not equal to j
                if s_hashmap[i] != j:
                    # If the mapping is invalid, return False
                    return False
            else:
                # If i is not in s_hashmap, add a mapping from i to j in s_hashmap
                s_hashmap[i] = j
                
            # Check if the character j from t is already in t_hashmap
            if j in t_hashmap:
                # If it is, check if the mapping in t_hashmap for j is not equal to i
                if t_hashmap[j] != i:
                    # If the mapping is invalid, return False
                    return False
            else:
                # If j is not in t_hashmap, add a mapping from j to i in t_hashmap
                t_hashmap[j] = i
        
        # If the loop completes without any invalid mappings, return True, indicating isomorphism
        return True
