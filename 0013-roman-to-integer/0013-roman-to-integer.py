class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = { 'I'      :       1,
                    'V'       :      5,
                    'X'        :     10,
                    'L'          :   50,
                    'C'           :  100,
                    'D'            : 500,
                    'M'             :1000,

        }
        res = 0
        pre_val = 0
        n = len(s)
        for i in range(n-1,-1,-1):
            if hashmap[s[i]] >= pre_val:
                res += hashmap[s[i]]
            else:
                res -= hashmap[s[i]]
            pre_val = hashmap[s[i]]
        return res