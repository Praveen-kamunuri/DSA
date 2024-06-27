class Solution:
    def intToRoman(self, num: int) -> str:
        
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        sym = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        
        i = 0
        res = ''
        while num > 0:
            
            while num >= val[i]:
                
                res += sym[i]
                num -= val[i]
                
            i += 1
        return res