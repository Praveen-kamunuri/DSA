class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {
                        'I'      :      1,
                        'V'      :      5,
                        'X'      :      10,
                        'L'      :      50,
                        'C'      :      100,
                        'D'      :      500,
                        'M'      :      1000,
            
                 }
        res = 0
        prev_val = 0
        for i in reversed(s):
            if hashmap[i] >= prev_val:
                res += hashmap[i]
            else:
                res -= hashmap[i]
            prev_val = hashmap[i]
        return res
        