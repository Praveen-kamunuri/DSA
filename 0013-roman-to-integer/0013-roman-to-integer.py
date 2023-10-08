class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {
            'I'      :       1,
            'V'      :       5,
            'X'      :       10,
            'L'      :       50,
            'C'      :       100,
            'D'      :       500,
            'M'      :       1000,

        }
        
        
        pre_val = 0
        res = 0
        
        for i in s[::-1]:
            if hashmap[i] >= pre_val:
                res += hashmap[i]
            else:
                res -= hashmap[i]
            
            pre_val = hashmap[i]
        return res
        