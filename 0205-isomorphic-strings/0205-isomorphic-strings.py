class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        
        s_hashmap = {}
        t_hashmap = {}
        
        for i, j in zip(s, t):
            if i in s_hashmap:
                if s_hashmap[i] != j:
                    return False
        
            else:
                s_hashmap[i] = j

            if j in t_hashmap:
                if t_hashmap[j] != i:
                    return False
            else:
                t_hashmap[j] = i

        return True
