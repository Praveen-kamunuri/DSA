class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        smap = {}
        tmap = {}

        for i in range(len(s)):
            if s[i] in smap:
                if smap[s[i]] != t[i]:
                    return False
            else:
                smap[s[i]] = t[i]
                tmap[t[i]] = s[i]

        return True